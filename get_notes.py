import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

registration_forum = 'vSikVyOdps' #found this id by running the get_venue_info script.


# Get all replies to the registration forum
notes = client.get_all_notes(forum=registration_forum)

# Create a dictionary with profile_id : [subject_area]
for n in notes:
    print(n)
