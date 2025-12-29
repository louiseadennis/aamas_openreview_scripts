import openreview
import client_object

client = client_object.client
venue_id_string = client_object.venue_id

response = client.request_expertise(
    name='AC_Scores',
    group_id=f'{venue_id_string}/Reviewers',
    venue_id=venue_id_string,
    alternate_match_group=f'{venue_id_string}/Senior_Area_Chairs',
    model='specter+mfr',
)

results = client.get_expertise_results(
    response,
    wait_for_complete=True
)

print(results)
