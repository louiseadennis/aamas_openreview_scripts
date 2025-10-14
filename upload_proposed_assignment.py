import openreview
import client_object
import sys

# if called with 1 as command line argument the proposed assigments will actually get posted to OpenReview
if sys.argv[1] == "1":
    print("uploading")

client = client_object.client
venue_id = client_object.venue_id
group = "Reviewers"
assignment_label = 'test'
assignment_invitation_name = 'reviewers_proposed_assignment_id'
# assignment_inviation_name = 'area_chairs_assignment_id' ?

venue_group = client.get_group(venue_id)

assignment_id = f'{venue_id}/{group}/-/Proposed_Assignment'
assignment_invitation_id = venue_group.content[assignment_invitation_name]['value']
#print(assignment_invitation_id)

assigned = {}
assigned["~Yasmin_Rafiq1"] = ['RfLVvCoGQ9']


for id in assigned.keys():
    print(str(id))
    for paper_id in assigned[id]:
        #print(paper_id)
        if (sys.argv[1] == "1"):
            client.post_edge(openreview.api.Edge(
            invitation=assignment_id,
            signatures=[venue_id],
            head=paper_id,
            tail=id,
            label=assignment_label,
            weight=1,
            ))
            print("posted")
    
                    
        

