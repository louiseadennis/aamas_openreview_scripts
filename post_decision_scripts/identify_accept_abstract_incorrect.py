import openreview
import client_object

client = client_object.client

venue_id = client_object.venue_id

reply_type = "Decision"
submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')


for submission in submissions:
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in submission.invitations):
        if (not f'{venue_id}/-/Withdrawn_Submission' in submission.invitations):
            decision = ""
            for reply in submission.details['replies']:
                for invitation in reply['invitations']:
                    if invitation.endswith(reply_type):
                        decision = reply['content']['decision']['value']
                        if decision == "Accept (Extended Abstract)":
                            try:
                                if submission.content['extended_abstract']['value']:
                                    print(submission.number)
                            except:
                                continue

