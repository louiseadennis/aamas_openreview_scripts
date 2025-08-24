import openreview
import client_object
import sys

client = client_object.client
venue_id = client_object.venue_id


venue_group = client.get_group(venue_id)

ac_ids = client.get_group(f'{venue_id}/Area_Chairs').members
ac_profiles = openreview.tools.get_profiles(client, ac_ids)

count = 0
for ac in ac_profiles:
    count = count + 1
    print(ac)
    
print(count)

                    
        

