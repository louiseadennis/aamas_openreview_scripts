import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

senior_area_chairs_proposed_assignment_id = f'{venue_id}/Senior_Area_Chairs/-/Proposed_Assignment'

venue_group = client.get_group(venue_id)

   
assignment_invitation_id = venue_group.content['senior_area_chairs_assignment_id']['value']
    
grouped_edges = client.get_grouped_edges(
    invitation = senior_area_chairs_proposed_assignment_id,
    groupby = 'label'
    )
    
sac_assignments = {}
for g_edge in grouped_edges:
    print("EDGE")
    print(g_edge['id']['label'])
    if (g_edge['id']['label'] == "Area Score Based Assignment"):
        for assignment in g_edge['values']:
            submission = client.get_note(assignment['head'])
            title = submission.content['title']['value']
            print(title)
            sac = assignment['tail']
            if (sac in sac_assignments.keys()):
                sac_assignments[sac].append(title)
            else:
                sac_assignments[sac] =[title]
                
for sac in sac_assignments.keys():
    print(sac)
    print(sac_assignments.get(sac))
                    
        

