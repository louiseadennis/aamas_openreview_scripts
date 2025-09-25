import openreview
import client_object
import sys

client = client_object.client
venue_id = client_object.venue_id


venue_group = client.get_group(venue_id)


recruitement_notes = client.get_all_notes(invitation=f'{venue_id}/Reviewers/-/Recruitment')

count = 0
reviews = 0
for note in recruitement_notes:
    try:
        if (note.content['reduced_load']):
            count = count + 1
            reviews = reviews + int(note.content['reduced_load']['value'])
            print(note)
    except:
        continue

               
print(str(count) + " Reviewers have requested reduced load in total they can do " + str(reviews) + " reviews")
        

