import openreview
import client_object

client = client_object.client

venue_id = 'AAMAS/2026/Test'

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')

for note in submissions:
    print(note)
