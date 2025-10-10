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
#assigned["~Tan_Minh_Nguyen1"] = ['7S72yQrHPM']
assigned["~Kun_Shao1"] = ['Ze6oyg3CrL']
#assigned["~Angelo_Ferrando1"] = ['v35iSwOSaA', 'CDFeZ78IeK', 'ErIWNSKCPe', 'tp2SDvQscg', 'noXYiuYnnr', 'C3c6LB2va9', 'vn1dLug1RP', 'lvrAgARBsF', '47zGa5Daf5', 'vQ9x0AJkvL', '3aFr2AYMeY', 'JHUY0tW947', 'nO69we5cvq', 'JxR48BnA7H', 'YXZOWrmili', 'lsGI35nza2', 'mNZ6p3Q4CP', 'GCmDek25zu', '19LmKvjXHO', 'jGBnSMc2w3', 'clRQxZT0tX', 'OU3iJhwooj', 'lJCulKvex5', 'dENftcOE7V', 'fllVBnrUA4', 'MeH5N8ajFG', '925jxBN2sB', 'SnKqq6SmRW', 'eboOUNvGyz', '2Kg5kyScDL', 'b6SASYB9pF', 'rzji6KYas3', 'jl0FI7nivW', 'b3MW3aJIAf', 'I2i5v0VueY', '7RRIztzQwK', 'qte0fJttjP', 'QFAB969qPB']


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
    
                    
        

