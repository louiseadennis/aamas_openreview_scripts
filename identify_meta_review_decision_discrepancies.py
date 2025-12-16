import openreview
import client_object

client = client_object.client

venue_id = client_object.venue_id

reply_type = "Meta_Review" #also: "Meta_Review","Official_Comment", "Decision", "Rebuttal" etc.
reply_type2 = "Decision"
submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')

replies = [reply for submission in submissions for reply in submission.details['replies'] if any(invitation.endswith(reply_type) for invitation in reply['invitations'])]

#for reply in replies:
#	print(reply['replyto'])
#	print(reply['content']['recommendation']['value'])
#	print("\n")

for submission in submissions:
	if (not f'{venue_id}/-/Desk_Rejected_Submission' in submission.invitations):
        # print(note)
            if (not f'{venue_id}/-/Withdrawn_Submission' in submission.invitations):
                recommendation = ""
                decision = ""
                for reply in submission.details['replies']:
                    for invitation in reply['invitations']:
                        if invitation.endswith(reply_type):
                            recommendation = reply['content']['recommendation']['value']
                    #print(f"recommendation: {reply['content']['recommendation']['value']}")
                        elif invitation.endswith(reply_type2):
                            decision = reply['content']['decision']['value']
                    #print(f"decision: {reply['content']['decision']['value']}")
                if recommendation == "Accept (Oral)":
                    if decision != "Accept (Full)":
                        print(submission.number)
                        print(f"Recommendation: Full, Decision: {decision}\n")
                elif recommendation == "Accept (Poster)":
                    if decision != "Accept (Extended Abstract)":
                        print(submission.number)
                        print(f"Recommendation: Extended Abstract, Decision: {decision}\n")
                elif recommendation == "Reject":
                    if decision != "Reject":
                        print(submission.number)
                        print(f"Recommendation: Reject, Decision: {decision}\n")
                else:
                    print(submission.number)
                    print("No Meta Review\n")
