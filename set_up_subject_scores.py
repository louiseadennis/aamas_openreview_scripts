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
    submission_id = submission.id
    if 'area' in submission.content:
        submission_subject_area = submission.content['area']['value']
        print(f'submission: {submission.id}, subject area: {submission_subject_area}')
        # Check registrations for any value that matches s and print the corresponding key
        for reviewer_id, subject in registrations.items():
                print(f"Reviewer ID: {reviewer_id}, Subject: {subject}")
                client.post_edge(openreview.api.Edge(
                        invitation=f'{venue_id}/Reviewers/-/Subject_Score',
                        signatures=[venue_id],
                        head=submission_id,
                        tail=reviewer_id,
                        weight=1,
                        label=submission_subject_area
                ))

