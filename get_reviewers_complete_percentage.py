import openreview
import client_object
import sys

client = client_object.client
venue_id = client_object.venue_id

venue_group = client.get_group(venue_id)

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')

total_assignments = {}
complete_assignments = {}

for submission in submissions:
    number = submission.number
    try:
        r_ids = client.get_group(f'{venue_id}/Submission{number}/Reviewers').members
    except:
        continue
    for rev in r_ids:
        if rev in total_assignments.keys():
            total_assignments[rev] = total_assignments.get(rev) + 1
        else:
            total_assignments[rev] = 1
            complete_assignments[rev] = 0
    for review in submission.details['replies']:
            #print(review['signatures'][0])
        test = client.get_group(review['signatures'][0])
        if (test.members[0] in r_ids):
            complete_assignments[test.members[0]] = complete_assignments.get(test.members[0]) + 1
        
for rev in total_assignments.keys():
    print(rev)
    if complete_assignments.get(rev) != 0:
        print(complete_assignments.get(rev)/total_assignments.get(rev))
    else:
        print("NONE")
            

