import openreview
import client_object

client = client_object.client
venue_id = '/AAMAS/2026/Test'

reply_type = "Official_Review" #also: "Meta_Review","Official_Comment", "Decision", "Rebuttal" etc.
submissions = client.get_all_notes(invitation=f'{venue_id}/-/{submission_name}',details = 'replies')
replies = [reply for submission in submissions for reply in submission.details['replies'] if any(invitation.endswith(reply_type) for invitation in reply['invitations'])]

note_id = '' #where do I find this

note_to_delete = client.get_note(note_id)
time_now = openreview.tools.datetime_millis(dt.datetime.now())

client.post_note_edit(
    invitation=f'{venue_id}/-/Edit'.
    signatures=note_to_delete.signatures,
    note=openreview.api.Note(
        id=note_to_delete_id,
        content=note_to_delete.content,
        ddate=time_now
                             )
                    )
