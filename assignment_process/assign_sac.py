import openreview
import client_object
import sys

# if called with 1 as command line argument the proposed assigments will actually get posted to OpenReview
if sys.argv[1] == "1":
    print("posting")

client = client_object.client
venue_id = client_object.venue_id

venue_group = client.get_group(venue_id)

senior_area_chairs_assignment_id = f'{venue_id}/Senior_Area_Chairs/-/Assignment'
assignment_invitation_id = venue_group.content['senior_area_chairs_assignment_id']['value']
print(assignment_invitation_id)
sac_group_id = f'{venue_id}/Senior_Area_Chairs'

assigned = {}
# Assignment lists goes here.

for ac_id in assigned.keys():
    print(str(ac_id))
    for paper_id in assigned[ac_id]:
        #print(paper_id)
        if (sys.argv[1] == "1"):
        
            client.post_edge(openreview.api.Edge(
            invitation=senior_area_chairs_assignment_id,
            signatures=[venue_id],
            head=paper_id,
            tail=ac_id,
            weight=1,
            ))
            print("posted")
    
                    
        

