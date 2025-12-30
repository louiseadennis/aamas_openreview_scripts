import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')

for note in submissions:
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in note.invitations):
        if (not f'{venue_id}/-/Withdrawn_Submission' in note.invitations):
            try:
                if note.content['extended_abstract']['value']:
                    #print(note.content['extended_abstract']['value'])
                    print(note.number)
            except:
                continue
