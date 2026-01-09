import openreview
import client_object
import csv

client = client_object.client

venue_id = client_object.venue_id
client.impersonate(venue_id)

reply_type = "Decision"
submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')


first_cells = []

with open('industry_authors.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row:  # make sure the row isn't empty
            first_cells.append(row[0])


for submission in submissions:
     if (not f'{venue_id}/-/Desk_Rejected_Submission' in submission.invitations):
        # print(note)
            if (not f'{venue_id}/-/Withdrawn_Submission' in submission.invitations):
                decision = ""
                
                for reply in submission.details['replies']:
                    for invitation in reply['invitations']:
                        if invitation.endswith(reply_type):
                            decision = reply['content']['decision']['value']
                            
                if (decision == "Accept (Full)" or decision == "Accept (Extended Abstract)"):
                    author_ids = submission.content['authorids']['value']
                    profiles = openreview.tools.get_profiles(client, author_ids)
                    author_names = []
                    for profile in profiles:
                        names = profile.content['names']
                        #print(names)
                        fullname = ""
                        for name in names:
                            try:
                                if name['preferred']:
                                    fullname = name['fullname']
                            except:
                                fullname = name['fullname']
                        if fullname == "":
                            #print(profile)
                            fullname = names[0]['fullname']
                        #print(fullname)
                        if fullname in first_cells:
                            author_email = profile.get_preferred_email()
                            new_string = f'\"{fullname}\",{author_email}'
                            print(new_string)
                            
                       
                            
                            
                    
