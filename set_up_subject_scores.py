import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

registration_forum = 'qPSvv8g0mL' #found this id by looking at the URL on the registration form.


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
            registrations[profile_id] = n.content['area']['value']
        except:
            print(profile_id)
            print("no area")
    
# get all active submissions under review
venue_group = client.get_group(venue_id)
under_review_id = venue_group.content['submission_venue_id']['value']
submissions = client.get_all_notes(content={'venueid': under_review_id})

# the subject area field in the submission note may be different per venue, for this example we'll use 'subject_area'
for submission in submissions:
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in submission.invitations):
        submission_id = submission.id
        submission_subject_area = submission.content['area']['value']
        print(f'submission: {submission.id}, subject area: {submission_subject_area}')
        # Check registrations for any value that matches s and print the corresponding key
        for reviewer_id, subject in registrations.items():
            if (subject == submission_subject_area or (subject == 'Modelling and Simulation of Societies (SIM)' and submission_subject_area == 'Modelling and Simluation of Societies (SIM)')):
                    print(f"Reviewer ID: {reviewer_id}, Subject: {subject}, Submission Subject: {submission_subject_area}")
                    client.post_edge(openreview.api.Edge(
                                 invitation=f'{venue_id}/Area_Chairs/-/Subject_Score',
                                 signatures=[venue_id],
                                 head=submission_id,
                                 tail=reviewer_id,
                                 weight=1,
                                 label=submission_subject_area
                         ))

