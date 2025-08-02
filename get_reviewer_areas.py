import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

registration_forum = 'vSikVyOdps' #found this id by running the get_venue_info script.

# Get all replies to the registration forum
notes = client.get_all_notes(replyto=registration_forum)

# Create a dictionary with profile_id : [subject_area]
registrations = {}
for n in notes:
    signature = n.signatures[0]
    profile = client.get_profile(signature)
    profile_id = profile.id
    # print(n)
    try:
        registrations[profile_id] = n.content['area']['value']
    except:
        print(profile_id)
        print("no area")

for reviewer_id, subject in registrations.items():
    print(reviewer_id)
    print(subject)
