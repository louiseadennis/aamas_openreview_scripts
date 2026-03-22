import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')

print("ID,Nominated,Title,Score,Area,Student Paper")
for submission in submissions:
    decision = ""
    best_paper_nom = False
    review_score = 0
    review_count = 0
                
    if ('replies' in submission.details.keys()):
        #print(submission.content['title']['value'])
        for reply in submission.details['replies']:
            for invitation in reply['invitations']:
                    if invitation.endswith("Decision"):
                        decision = reply['content']['decision']['value']
                    if invitation.endswith("Official_Review"):
                        review_count = review_count + 1
                        if 'best_paper' in reply['content']:
                            best_paper_nom = True
                        review_score = review_score + reply['content']['rating']['value']
                     
        if (review_count > 0):
            average_score = review_score / review_count
        else:
            average_score = 0
                                
        if (decision == "Accept (Full)"):
            #print(submission.content)
            if ('value' in submission.content['student_paper'].keys()):
                student = submission.content['student_paper']['value'][0]
            else:
                student = "No"
            if (best_paper_nom):
                print(str(submission.number) + ",1,\"" + submission.content['title']['value'] + "\"," + str(average_score) + ",\"" + submission.content['area']['value'] + "\"," + student)
            elif (average_score >= 7.0):
                print(str(submission.number) + ",0,\"" + submission.content['title']['value'] + "\"," + str(average_score) + ",\"" + submission.content['area']['value'] + "\"," + student)

               
