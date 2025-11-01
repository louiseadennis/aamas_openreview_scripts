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
        # profile = client.get_profile(signature)
        # profile_id = profile.id
        if (ac.id == signature):
            flag = True
            break
    if (not flag):
        if ac.id.startswith("~"):
            print(ac.id + " Gen AI Reminder")
            subject = 'AAMAS 2026 Reminder of our Generative AI Policy'
            message = 'We will shortly be assigning papers to you in your role as AAMAS PC.  You never completed the AAMAS PC registration form and so never confirmed that you accepted the AAMAS policy on the use of Generative AI in reviewing.  This policy states that reviewers should not use AI to write the substance of their review, though they may use it to polish prose.  Reviewers may not, under any circumstances, upload any paper submitted to AAMAS to a generative AI tool since this breaches confidentiality.\n\n Even though you have not confirmed adherence to this policy, abiding by it is a condition of continuing in your role as AAMAS PC.\n\n Please let us know if you are not prepared to follow this policy and we will reassign your papers.\n\n Many Thanks \n\n Louise & Chris'
        else:
            print(ac.id + " Apology")
            subject = 'AAMAS 2026 Unable to Assign a Reviewer Role'
            message = 'Thank you for agreeing to serve as AAMAS PC.  Unfortunately we are unable to assign papers to reviewers who have not linked their email address to an OpenReview profile, which is the case for you.\n\n We anticipate that we will be looking for emergency reviewers between the 14th and 21st November, so if you are prepared to serve in this role, please link your email address to your open review profile and let us know.\n\n Many Thanks \n\n Louise & Chris'
        recipients = [ac.id]
        invitation = f'{venue_id}/-/Edit'
        if sys.argv[1] == "1":
            client.post_message(subject, recipients, message, invitation=invitation)

