import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')
edit_invitation=f'{venue_id}/-/Edit'

area = 'Robotics and Control (ROBOT)'
keyword = 'ROBOT'

for note in submissions:
    #print(note.content['area']['value'])
    try:
        if note.content.get("area").get('value') == area:
            keywords = note.content.get('keywords').get('value')
            if 'IA' not in keywords:
                #print(note)
                print(keyword + ' not in keywords')
                keywords.append(keyword)
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
