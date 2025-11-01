import openreview
import client_object
import sys

if sys.argv[1] == "1":
    print("posting")

client = client_object.client
venue_id = client_object.venue_id

ac_profiles = []

# Create a dictionary with profile_id : [subject_area]
for ac in ac_profiles:
    print(ac.id + " Sending Message")
    subject = 'Message Subject'
    message = 'Message Body'
    recipients = [ac.id]
    invitation = f'{venue_id}/-/Edit'
    if sys.argv[1] == "1":
        client.post_message(subject, recipients, message, invitation=invitation)

