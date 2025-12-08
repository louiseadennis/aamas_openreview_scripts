import openreview
import client_object
import sys


client = client_object.client
venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')
#submissions2 = client.get_all_notes(invitation=f'{venue_id}/-/Submission')


for note in submissions:
    #print("a")
    if (f'{venue_id}/-/Desk_Rejected_Submission' in note.invitations):
        print(note.content['authorids']['value'])
