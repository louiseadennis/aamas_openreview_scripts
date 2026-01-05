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
    print(ac + " Sending Message")
    subject = 'AAMAS 2026 Review Check In'
    message = 'Dear {{fullname}}, \n\n The AAMAS review system currently shows that you have completed none of the reviews assigned to you.  Can you please check in by emailing louise.dennis@manchester.ac.uk to confirm that you are aware that the review deadline is this Friday, 14th November, and that you anticipate being able to complete your review assignment by that deadline.\n\n  All the best,\n\n Louise and Chris'
    recipients = [ac]
    invitation = f'{venue_id}/-/Edit'
    if sys.argv[1] == "1":
        client.post_message(subject, recipients, message, invitation=invitation)

