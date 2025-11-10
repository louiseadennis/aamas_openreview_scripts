import openreview
import client_object
import sys

client = client_object.client
venue_id = client_object.venue_id

venue_group = client.get_group(venue_id)

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')

total_assignments = {}
complete_assignments = {}
no_reviews = []

no_reviews_done = []
for submission in submissions:
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in submission.invitations):
        possible_issue = False
        number = submission.number
        try:
            r_ids = client.get_group(f'{venue_id}/Submission{number}/Reviewers').members
        except:
            continue
        for rev in r_ids:
            if rev in no_reviews_done:
                no_reviews.append(number)

no_reviews.sort()
            
for issue in no_reviews:
    print(issue)
