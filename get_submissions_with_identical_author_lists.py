import openreview
import client_object
import sys


client = client_object.client
venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')
#submissions2 = client.get_all_notes(invitation=f'{venue_id}/-/Submission')


for note in submissions:
    #print("a")
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in note.invitations):
        for note2 in submissions:
            if (not f'{venue_id}/-/Desk_Rejected_Submission' in note2.invitations):
                #print("b")
                if (note.id != note2.id):
                                    #print(note.id)
                                    #print(note2.id)
                    good = False
                    for author_id in note.content['authorids']['value']:
                        if (author_id not in note2.content['authorids']['value']):
                            good = True
                                            #print("breaking 1")
                            break
                    if (not good):
                        for author_id in note2.content['authorids']['value']:
                            if (author_id not in note.content['authorids']['value']):
                                good = True
                                                #print("breaking 2")
                                break
                    if good:
                                        #print("breaking 3")
                        continue
                    else:
                        print(note.content['title']['value'])
                        print(note.content['authorids']['value'])
                        print(note2.content['title']['value'])
                        print(note2.content['authorids']['value'])
                        print(" ")
