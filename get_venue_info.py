import openreview
import client_object

client = client_object.client

venue_id = 'AAMAS/2026/Test'

venue_group = client.get_group(venue_id)
print(venue_group)
