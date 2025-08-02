import openreview
import client_object

# API V2
client = client_object.client

venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')
#gets the desk rejection name of the invitation
desk_rejection_name = client.get_group(venue_id).content['desk_rejection_name']['value']
    
# for each submission note that does not contain a pdf field, post a desk rejection note
for submission in submissions:
    #Check for a pdf field value
    if not submission.content.get('pdf', {}).get('value'):
        desk_reject_note = client.post_note_edit(
                    #desk rejection invitation
                    invitation=f'{venue_id}/Submission{submission.number}/-/{desk_rejection_name}',
                    signatures=[f'{venue_id}/Program_Chairs'],
                    note=openreview.api.Note(
                        content = {
                        'desk_reject_comments': { 'value': 'No PDF.' }
                        }
                    )
                )
        print(submission.number, "is desk rejected")
