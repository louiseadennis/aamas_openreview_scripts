import openreview
import client_object

client = client_object.client

venue_id = client_object.venue_id

reply_type = "Decision"
submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')


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
                    title = submission.content['title']['value']
                    author_ids = submission.content['authorids']['value']
                    profiles = openreview.tools.get_profiles(client, author_ids)
                    author_names = []
                    submission_string = f'{title} - {decision}\n'
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
                        new_string = f'\"{fullname}\",'
                        author_names.append(fullname)
                        
                        institutions = []
                        try:
                            history = profile.content['history']
                                                    #print(history)
                            for position in history:
                                                        #print(position['end'])
                                if position['end'] == None:
                                                            #print("hello")
                                                            #print(position['institution'])
                                    name = position['institution']['name']
                                                            #print(name)
                                    institutions.append(name)
                                elif position['end'] > 2025:
                                    institutions.append(position['institution']['name'])
                        except Exception as e:
                            print(e)
                                    
                        author_string = f'\t{fullname}: {institutions}\n'
                        submission_string = submission_string + author_string
                    print(submission_string)
                            
                       
                            
                            
                    
