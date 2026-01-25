import openreview
import client_object

client = client_object.client

venue_id = client_object.venue_id
client.impersonate(venue_id)

reply_type = "Decision"
submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')


for submission in submissions:
             #if (not f'{venue_id}/-/Desk_Rejected_Submission' in submission.invitations):
        # print(note)
                  #  if (not f'{venue_id}/-/Withdrawn_Submission' in submission.invitations):
                decision = ""
                
                for reply in submission.details['replies']:
                    for invitation in reply['invitations']:
                        if invitation.endswith(reply_type):
                            decision = reply['content']['decision']['value']
                            
                if (decision == "Accept (Full)" or decision == "Accept (Extended Abstract)"):
                    title = submission.content['title']['value']
                    author_ids = submission.content['authorids']['value']
                    profiles = openreview.tools.get_profiles(client, author_ids)
                    author_names = []
                    author_list = []
                    author_id_to_name = {}
                    author_id_to_email = {}
                    for profile in profiles:
                        found_name = False
                                    # print(profile)
                        username = profile.id
                        if (username not in author_ids):
                            for name in profile.content['names']:
                                if name['username'] in author_ids:
                                    username = name['username']
                        for name in profile.content['names']:
                            if ('preferred' in name.keys() and name['preferred']):
                                #print("adding1 " + username)
                                author_id_to_name[username] = name['fullname']
                                found_name = True
                                break
                        if (not found_name):
                            #print("adding " + username)
                            author_id_to_name[username] = profile.content['names'][0]['fullname']
                        author_email = profile.get_preferred_email()
                        author_id_to_email[username] = author_email

                    for id in author_ids:
                        fullname = author_id_to_name[id]
                        author_email = author_id_to_email[id]

                        new_string = f'\"{fullname}\",'
                        email_string = f'\"{author_email}\"'
                        author_names.append(fullname)
                        author_names.append(email_string)
                            
                    author_string = ",".join(author_names)
                    print(f'{submission.number},{decision},\"{title}\",{author_string}')

