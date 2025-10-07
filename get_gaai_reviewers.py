import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

registration_forum = 'sMKm6zUMyk' #You find this by looking at the URL form?id=... when you click on the Reviewer Registration button....


# Get all replies to the registration forum
notes = client.get_all_notes(replyto=registration_forum)

# Create a dictionary with profile_id : [subject_area]
registrations = {}
for n in notes:
    signature = n.signatures[0]
    profile = client.get_profile(signature)
    profile_id = profile.id
    if (not profile_id in registrations):
        try:
            area = n.content['area']['value']
            if (area == "Generative and Agentic AI (GAAI)"):
                print(profile_id)
                print(n.content['area']['value'])
        except:
            print(profile_id)
            print("no area")
    
