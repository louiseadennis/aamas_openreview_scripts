import openreview
import client_object
import pc_subject_scores

subject_score = pc_subject_scores.subject_score

client = client_object.client
venue_id = client_object.venue_id

# get all active submissions under review
venue_group = client.get_group(venue_id)

# the subject area field in the submission note may be different per venue, for this example we'll use 'subject_area'
for submission_id in subject_score.keys():
    for reviewer_id in subject_score.get(submission_id):
        print(f"Reviewer ID: {reviewer_id}, submission: {submission_id}")
        client.post_edge(openreview.api.Edge(
                    invitation=f'{venue_id}/Reviewers/-/Subject_Score',
                    signatures=[venue_id],
                    head=submission_id,
                    tail=reviewer_id,
                    weight=1,
                    label="Area Match"
                    # label=submission_subject_area
        ))
