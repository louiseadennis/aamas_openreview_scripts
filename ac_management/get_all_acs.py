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
    # print(ac)
    
    ac_string = ""
    found_name = False
    for name in ac.content['names']:
        if ('preferred' in name.keys() and name['preferred']):
            ac_string = ac_string + name['fullname']
            found_name = True
            break
    if (not found_name):
        ac_string = ac_string + ac.content['names'][0]['fullname']
    
    if ('history' in ac.content.keys() and ac.content['history']):
            history = ac.content['history'][0]
            institution = history['institution']['name']
            
            ac_string = ac_string + ", " + institution
            
    print(ac_string)

    
#print(count)

                    
        

