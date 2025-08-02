import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

venue_group = client.get_group(venue_id)
print(venue_group)
