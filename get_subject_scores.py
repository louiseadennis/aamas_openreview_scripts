import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id


venue_group = client.get_group(venue_id)
subject_score_invitation_id = f'{venue_id}/Area_Chairs/-/Subject_Score'

grouped_edges = client.get_grouped_edges(
    invitation = subject_score_invitation_id,
    groupby = 'tail'
                                         )
                                         
for group in grouped_edges:
    print(group)
