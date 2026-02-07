import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')

count = 0
for submission in submissions:
    decision = ""
                
    if ('replies' in submission.details.keys()):
        #print(submission.content['title']['value'])
        for reply in submission.details['replies']:
            for invitation in reply['invitations']:
                    if invitation.endswith("Decision"):
                        decision = reply['content']['decision']['value']
                                
        if (decision == "Accept (Full)" or decision == "Accept (Extended Abstract)"):
            if ('value' in submission.content['student_paper'].keys()):
                #print(submission.content['student_paper']['value'])
                if ('The primary author is a student.' in submission.content['student_paper']['value']):
                    print(submission.content['title']['value'])
                    print(submission.content['student_paper'])
                    count = count + 1
print(count)


