import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

max_papers_id = f'{venue_id}/Reviewers/-/Custom_Max_Papers'

edges = client.get_grouped_edges(
    invitation=max_papers_id,
    groupby = 'tail'
)

for edge in edges:
    print(edge['id']['tail'] + " = " + str(edge['values'][0]['weight']))
