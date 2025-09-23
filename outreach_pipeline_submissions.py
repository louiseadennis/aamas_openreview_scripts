import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')

pipeline_count = 0
for note in submissions:
    if 'workshop_outreach_pipeline' in note.content:
        pipeline_count = pipeline_count + 1
        print(note.content['title']['value'])
        if 'workshop_name' in note.content:
            print(note.content['workshop_name']['value'])
        else:
            print("no workshop given")
        
