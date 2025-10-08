import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

# registration_forum = 'vSikVyOdps' #found this id by running the get_venue_info script.
registrations = {}
registrations['~Jaime_Sichman1'] = 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)'
registrations['~Nirav_Ajmeri1'] = 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)'
registrations['~Reyhan_Aydoğan1'] = 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)'
registrations['~Leandro_Buss_Becker1'] = 'Engineering and Analysis of Multiagent Systems (EMAS)'
registrations['~Angelo_Ferrando1'] = 'Engineering and Analysis of Multiagent Systems (EMAS)'
registrations['~Zahia_Guessoum1'] = 'Engineering and Analysis of Multiagent Systems (EMAS)'
registrations['~Prashant_Doshi1'] = 'Generative and Agentic AI (GAAI)'
registrations['~Kate_Larson1'] = 'Generative and Agentic AI (GAAI)'
registrations['~Karl_Tuyls1'] = 'Generative and Agentic AI (GAAI)'
registrations['~Niclas_Boehmer1'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Noam_Hazon1'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Omer_Lev1'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Minming_Li1'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Shuai_Li3'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Neeldhara_Misra1'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Svetlana_Obraztsova1'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Maria_Silvia_Pini2'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Alan_Tsang1'] = 'Game Theory and Economic Paradigms (GTEP)'
registrations['~Beatrice_Biancardi1'] = 'Human-Agent Interaction (HAI)'
registrations['~Brittany_Duncan1'] = 'Human-Agent Interaction (HAI)'
registrations['~Matthias_Scheutz1'] = 'Human-Agent Interaction (HAI)'
registrations['~Zehong_Cao1'] = 'Innovative Applications (IA)'
registrations['~Gauthier_Picard2'] = 'Innovative Applications (IA)'
registrations['~Karthik_Abinav_Sankararaman1'] = 'Learning and Adaptation (LEARN)'
registrations['~Bo_An2'] = 'Learning and Adaptation (LEARN)'
registrations['~Vincent_Corruble1'] = 'Learning and Adaptation (LEARN)'
registrations['~Francisco_Cruz1'] = 'Learning and Adaptation (LEARN)'
registrations['~Yali_Du1'] = 'Learning and Adaptation (LEARN)'
registrations['~Ferdinando_Fioretto1'] = 'Learning and Adaptation (LEARN)'
registrations['~Sarah_Keren1'] = 'Learning and Adaptation (LEARN)'
registrations['~Yasser_Mohammad1'] = 'Learning and Adaptation (LEARN)'
registrations['~Tan_Minh_Nguyen1'] = 'Learning and Adaptation (LEARN)'
registrations['~Kun_Shao1'] = 'Learning and Adaptation (LEARN)'
registrations['~Nicola_Basilico1'] = 'Robotics and Control (ROBOT)'
registrations['~Maria_L._Gini1'] = 'Robotics and Control (ROBOT)'
registrations['~Roberta_Calegari1'] = 'Representation and Reasoning (RR)'
registrations['~Brian_Logan1'] = 'Representation and Reasoning (RR)'
registrations['~Maria_Vanina_Martinez1'] = 'Representation and Reasoning (RR)'
registrations['~Valentina_A._M._Tamma1'] = 'Representation and Reasoning (RR)'
registrations['~Shah_Jamal_Alam1'] = 'Modelling and Simluation of Societies (SIM)'
registrations['~Franziska_Klügl1'] = 'Modelling and Simluation of Societies (SIM)'
registrations['~Fabian_Lorig1'] = 'Modelling and Simluation of Societies (SIM)'
registrations['~Filippo_Bistaffa1'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'
registrations['~Roni_Stern1'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'
registrations['~Roman_Barták1'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'
registrations['~Sara_Bernardini1'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'


# Get all replies to the registration forum
# notes = client.get_all_notes(replyto=registration_forum)

# Create a dictionary with profile_id : [subject_area]
# registrations = {}
# for n in notes:
 #    signature = n.signatures[0]
  #   profile = client.get_profile(signature)
   #  profile_id = profile.id
    # if (not profile_id in registrations):
      #   try:
        #     registrations[profile_id] = n.content['area']['value']
        # except:
          #   print(profile_id)
      #       print("no area")
    
# get all active submissions under review
venue_group = client.get_group(venue_id)
under_review_id = venue_group.content['submission_venue_id']['value']
submissions = client.get_all_notes(content={'venueid': under_review_id})

# the subject area field in the submission note may be different per venue, for this example we'll use 'subject_area'
for submission in submissions:
    submission_id = submission.id
    if 'area' in submission.content:
        submission_subject_area = submission.content['area']['value']
        print(f'submission: {submission.id}, subject area: {submission_subject_area}')
        # Check registrations for any value that matches s and print the corresponding key
        for reviewer_id, subject in registrations.items():
                if submission_subject_area == subject:
                    print(f"Reviewer ID: {reviewer_id}, Subject: {subject}")
                    client.post_edge(openreview.api.Edge(
                                 invitation=f'{venue_id}/Senior_Area_Chairs/-/Subject_Score',
                                 signatures=[venue_id],
                                 head=submission_id,
                                 tail=reviewer_id,
                                 weight=1,
                                 label=submission_subject_area
                    ))

