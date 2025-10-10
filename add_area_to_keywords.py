import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')
edit_invitation=f'{venue_id}/-/Edit'

for note in submissions:
    #print(note.content['area']['value'])
    try:
        if note.content.get("area").get('value') == 'Learning and Adaptation (LEARN)':
            keywords = note.content.get('keywords').get('value')
            if 'LEARN' not in keywords:
                #print(note)
                print('LEARN not in keywords')
                keywords.append('LEARN')
                print(keywords)
                content = note.content
                content.get('keywords').update({'value': keywords})
                print(content['title']['value'])
                client.post_note_edit(invitation=edit_invitation,
                                        signatures=[venue_id],
                                        note=openreview.api.Note(
                                        id=note.id,
                                        readers=note.readers,
                                        content=content
                                                                 )
                                                                 )
                print("updated")
    except:
        print("no area")
