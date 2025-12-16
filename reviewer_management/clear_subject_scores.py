import openreview
import client_object
import datetime

client = client_object.client
venue_id = client_object.venue_id


venue_group = client.get_group(venue_id)
subject_score_invitation_id = f'{venue_id}/Area_Chairs/-/Subject_Score'

grouped_edges = client.get_grouped_edges(
    invitation = subject_score_invitation_id,
    groupby = 'tail'
                                         )
                                         
for group in grouped_edges:
    for edge in group['values']:
        print(edge)
        edge_id = edge['id']
        time_now = openreview.tools.datetime_millis(datetime.datetime.now())
            
        edge = client.get_edge(edge_id)
        edge.ddate = time_now
        edge.signatures = [venue_id]
        edge.nonreaders = None
        client.post_edge(edge)
