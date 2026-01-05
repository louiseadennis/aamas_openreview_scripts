import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

edit_invitation=f'{venue_id}/-/Edit'

reply_type = "Decision"
submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')


# area = 'Engineering and Analysis of Multiagent Systems (EMAS)'
keyword_list = ['EMAS', 'GAAI', 'LEARN', 'COINE', 'GTEP', 'SOPS', 'RR', 'SIM', 'HAI', 'ROBOT', 'IA']

for note in submissions:
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in note.invitations):
        if (not f'{venue_id}/-/Withdrawn_Submission' in note.invitations):
            for reply in note.details['replies']:
                for invitation in reply['invitations']:
                    if invitation.endswith(reply_type):
                            decision = reply['content']['decision']['value']
                            if (decision == "Accept (Full)" or decision == "Accept (Extended Abstract)"):
                                try:
                                    keywords = note.content.get('keywords').get('value')
                                    for keyword in keyword_list:
                                        if keyword in keywords:
                                            print(keyword)
                                            print(keyword + ' in keywords')
                                            keywords.remove(keyword)
                                            print(keywords)
                                            content = note.content
                                            content.get('keywords').update({'value': keywords})
                                                                                    #print(content['title']['value'])
                                            client.post_note_edit(invitation=edit_invitation,
                                                    signatures=[venue_id],
                                                    note=openreview.api.Note(
                                                            id=note.id,
                                                            readers=note.readers,
                                                            content=content))
                                                                                            
                                            print("updated")
                                except:
                                    print("no area")
