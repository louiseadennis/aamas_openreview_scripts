import openreview
import client_object
import sys


client = client_object.client
venue_id = client_object.venue_id

registration_forum = 'qPSvv8g0mL' #found this id by running the get_venue_info script.


# Get all replies to the registration forum
notes = client.get_all_notes(forum=registration_forum)

ac_ids = client.get_group(f'{venue_id}/Area_Chairs').members
ac_profiles = openreview.tools.get_profiles(client, ac_ids)

bad_acs = []
# Create a dictionary with profile_id : [subject_area]
for ac in ac_profiles:
    flag = False
    for n in notes:
        signature = n.signatures[0]
        try:
            profile = client.get_profile(signature)
            profile_id = profile.id
            if (ac.id == profile_id):
                flag = True
        except:
            continue

    if (not flag):
        print(ac.id)
        print("no area")
    else:
        print(ac.id)
        print("has registration notes")

