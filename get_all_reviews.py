import openreview
import client_object

client = client_object.client

venue_id = 'AAMAS/2026/Test'

reply_type = "Official_Review" #also: "Meta_Review","Official_Comment", "Decision", "Rebuttal" etc.
submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')

replies = [reply for submission in submissions for reply in submission.details['replies'] if any(invitation.endswith(reply_type) for invitation in reply['invitations'])]

#print(replies)
