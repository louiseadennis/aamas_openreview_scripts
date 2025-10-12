import openreview
import client_object
import ac_subject_scores

client = client_object.client
venue_id = client_object.venue_id

#registration_forum = 'sMKm6zUMyk' #found this id by looking at the URL on the registration form.

registrations = {}
registrations['~Aniello_Murano1'] = 'Representation and Reasoning (RR)'
registrations['~Charles_Lesire2'] = 'Innovative Applications (IA)'
registrations['~Edith_Elkind1'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Enrico_Scala3'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'
registrations['~Joana_Campos1'] = 'Human-Agent Interaction (HAI)'
registrations['~K._Brent_Venable1'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Marco_Maratea3'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'
registrations['~Nadia_Abchiche-Mimouni1'] = 'Learning and Adaptation (LEARN)'
registrations['~Natasha_Alechina1']  = 'Representation and Reasoning (RR)'
registrations['~Qi_Qi2'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Robert_Bredereck1'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Sarath_Sreedharan1'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'
registrations['~Shiwali_Mohan1'] = 'Learning and Adaptation (LEARN)'
registrations['~Tal_Kachman1'] = 'Generative and Agentic AI (GAAI)'
registrations['~Victor_Sanchez-Anguix1'] = 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)'
registrations['trp@liv.ac.uk'] = 'Representation and Reasoning (RR)'

# Get all replies to the registration forum
# notes = client.get_all_notes(replyto=registration_forum)

# Create a dictionary with profile_id : [subject_area]
# registrations = {}
# for n in notes:
 #     signature = n.signatures[0]
  #    profile = client.get_profile(signature)
#      profile_id = profile.id
#      if (not profile_id in registrations):
 #         try:
  #            registrations[profile_id] = n.content['area']['value']
   #       except:
    #          print(profile_id)
     #         print("no area")
    
# get all active submissions under review
venue_group = client.get_group(venue_id)
under_review_id = venue_group.content['submission_venue_id']['value']
submissions = client.get_all_notes(content={'venueid': under_review_id})

scores = {}

# the subject area field in the submission note may be different per venue, for this example we'll use 'subject_area'
for submission in submissions:
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in submission.invitations):
        submission_id = submission.id
        scores[submission_id] = []
        submission_subject_area = submission.content['area']['value']
                # print(f'submission: {submission.id}, subject area: {submission_subject_area}')
        # Check registrations for any value that matches s and print the corresponding key
        for reviewer_id, subject in registrations.items():
            if (subject == submission_subject_area or (subject == 'Modelling and Simulation of Societies (SIM)' and submission_subject_area == 'Modelling and Simluation of Societies (SIM)')):
                    #print(f"Reviewer ID: {reviewer_id}, Subject: {subject}, Submission Subject: {submission_subject_area}")
                    scores.get(submission_id).append(reviewer_id)
                    #client.post_edge(openreview.api.Edge(
                    #             invitation=f'{venue_id}/Area_Chairs/-/Subject_Score',
                    #             signatures=[venue_id],
                    #             head=submission_id,
                    #             tail=reviewer_id,
                    #             weight=1,
                    #             label=submission_subject_area
                    #     ))

for submission_id in scores.keys():
    print("subject_score[\"" + submission_id + "\"] = " + str(scores.get(submission_id)))
    print("\n")
