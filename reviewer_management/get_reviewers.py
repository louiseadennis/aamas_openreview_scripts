import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

pc_ids = client.get_group(f'{venue_id}/Reviewers').members
pc_profiles = openreview.tools.get_profiles(client, pc_ids)

for pc in pc_profiles:
    print(pc)
