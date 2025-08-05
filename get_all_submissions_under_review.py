import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

print("This doesn't seem to work now I've reset dev site.")

venue_group = client.get_group(venue_id)
under_review_id = venue_group.content['submission_venue_id']['value']
submissions = client.get_all_notes(content={'venueid': under_review_id})

for submission in submissions:
    print(submission)
