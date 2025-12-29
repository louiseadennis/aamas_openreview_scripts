import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

group = 'Reviewers'

proposed_assignment_id = f'{venue_id}/{group}/-/Proposed_Assignment'

venue_group = client.get_group(venue_id)

#assignment_invitation_id = venue_group.content['proposed_assignment_id']['value']
    
grouped_edges = client.get_grouped_edges(
    invitation = proposed_assignment_id,
    groupby = 'label'
    )
    
assignments = {}
for g_edge in grouped_edges:
    print(g_edge['id']['label'])
    if (g_edge['id']['label'] == "test"):
        for assignment in g_edge['values']:
            submission = client.get_note(assignment['head'])
            title = submission.content['title']['value']
            #print(title)
            person = assignment['tail']
            if (person in assignments.keys()):
                assignments[person].append(title)
            else:
                assignments[person] =[title]
                
for person in assignments.keys():
    print(person)
    print(assignments.get(person))
                    
        

