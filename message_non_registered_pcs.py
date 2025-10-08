import openreview
import client_object
import sys

if sys.argv[1] == "1":
    print("posting")


client = client_object.client
venue_id = client_object.venue_id

ac_ids = client.get_group(f'{venue_id}/Reviewers').members
ac_profiles = openreview.tools.get_profiles(client, ac_ids)


registration_forum = 'sMKm6zUMyk' #You find this by looking at the URL form?id=... when you click on the Reviewer Registration button....


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
            break
    if (not flag):
        print(ac.id)
        subject = 'AAMAS 2026 Please Complete Registration Tasks'
        message = 'To help with paper bidding we need you to complete our registration form with the area in which you feel you have the most expertise.  In OpenReview you can find this in your Reviewer Console under Pending Tasks.  \n\n We also need you to confirm you will abide by our policy on the use of generative AI in reviews.  \n\n If you can\'t see a Reviewer Console or Pending Tasks then it is possible that the email where you are recieving this message is not connected to your OpenReview profile.  Please add this email to your profile if that is the case.\n\n Many Thanks \n\n Louise & Chris'
        recipients = [ac.id]
        invitation = f'{venue_id}/-/Edit'
        if sys.argv[1] == "1":
            client.post_message(subject, recipients, message, invitation=invitation)

