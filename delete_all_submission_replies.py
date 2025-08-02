import openreview
import client_object
import datetime

client = client_object.client
venue_id = 'AAMAS/2026/Test'

#reply_type = "Official_Review" #also: "Meta_Review","Official_Comment", "Decision", "Rebuttal" etc.
submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')

replies = [reply for submission in submissions for reply in submission.details['replies']]

for review in replies:
    note_id = review['id']

    note_to_delete = client.get_note(note_id)
    time_now = openreview.tools.datetime_millis(datetime.datetime.now())

    client.post_note_edit(
        invitation=f'{venue_id}/-/Edit',
        signatures=note_to_delete.signatures,
        note=openreview.api.Note(
            id=note_to_delete.id,
            content=note_to_delete.content,
            ddate=time_now
                             )
                    )
