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
print(grouped_edges)
                    
        

