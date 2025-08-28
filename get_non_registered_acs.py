import openreview
import client_object
import sys

client = client_object.client
venue_id = client_object.venue_id

ac_ids = client.get_group(f'{venue_id}/Senior_Area_Chairs').members
ac_profiles = openreview.tools.get_profiles(client, ac_ids)


registration_forum = 'vSikVyOdps' #found this id by running the get_venue_info script.


# Get all replies to the registration forum
notes = client.get_all_notes(replyto=registration_forum)

# Create a dictionary with profile_id : [subject_area]
for ac in ac_profiles:
    flag = False
    for n in notes:
        signature = n.signatures[0]
        profile = client.get_profile(signature)
        profile_id = profile.id
        if (ac.id == profile_id):
            flag = True
    if (not flag):
        subject = 'AAMAS 2026 Please Complete Registration Tasks'
        message = 'In order to match Senior Program Committee appropriately to papers we need you to complete our registration form with the area you are reviewing for.  In OpenReview you can find this in your Area Chair Console under Pending Tasks.  Please can you fill this in before we assign papers.  You should be able to find your area in your original invitation message.\n\n We also need you to confirm you will abide by our policy on the use of generative AI in reviews.  \n\n Many Thanks \n\n Louise & Chris'
        recipients = [ac.id]
        invitation = f'{venue_id}/-/Edit'
        client.post_message(subject, recipients, message, invitation=invitation)

