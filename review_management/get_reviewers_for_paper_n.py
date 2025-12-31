import openreview
import client_object
import sys

number = sys.argv[1]

client = client_object.client
venue_id = client_object.venue_id

venue_group = client.get_group(venue_id)

r_ids = client.get_group(f'{venue_id}/Submission{number}/Reviewers').members
submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')

for r_id in r_ids:
    print(r_id)
    
print("Those with Completed Reviews")
for submission in submissions:
    if str(submission.number) == number:
        for review in submission.details['replies']:
            #print(review['signatures'][0])
            test = client.get_group(review['signatures'][0])
            print(test.members[0])
            

