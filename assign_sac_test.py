import openreview
import client_object
import sys

posting = False
# if called with 1 as command line argument the proposed assigments will actually get posted to OpenReview

client = client_object.client
venue_id = client_object.venue_id

# Create a dictionary with profile_id : [subject_area]
registrations = {}
areas = {}
registrations['~Jaime_Sichman1'] = 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)'
registrations['~Nirav_Ajmeri1'] = 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)'
registrations['~Reyhan_Aydoğan1'] = 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)'
registrations['leandro.becker@ufsc.br'] = 'Engineering and Analysis of Multiagent Systems (EMAS)'
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
registrations['valli@liverpool.ac.uk'] = 'Representation and Reasoning (RR)'
registrations['~Shah_Jamal_Alam1'] = 'Modelling and Simluation of Societies (SIM)'
registrations['~Franziska_Klügl1'] = 'Modelling and Simluation of Societies (SIM)'
registrations['~Fabian_Lorig1'] = 'Modelling and Simluation of Societies (SIM)'
registrations['~Filippo_Bistaffa1'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'
registrations['~Roni_Stern1'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'
registrations['~Roman_Barták1'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'
registrations['~Sara_Bernardini1'] = 'Search, Optimization, Planning, and Scheduling (SOPS)'



area_list = {'Engineering and Analysis of Multiagent Systems (EMAS)','Generative and Agentic AI (GAAI)', 'Learning and Adaptation (LEARN)', 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)', 'Game Theory and Economic Paradigms (GTEP)', 'Search, Optimization, Planning, and Scheduling (SOPS)', 'Representation and Reasoning (RR)', 'Modelling and Simluation of Societies (SIM)', 'Human-Agent Interaction (HAI)', 'Robotics and Control (ROBOT)',
                    'Innovative Applications (IA)'}

for area in area_list:
    # print(area)
    areas[area] = []
    
for sac in registrations.keys():
    #print(sac)
    area = registrations.get(sac)
    #print(area)
    areas.get(area).append(sac)
    #print(areas.get(area))

acs = {}

# senior_area_chairs_assignment_id = f'{venue_id}/Senior_Area_Chairs/-/Assignment'

venue_group = client.get_group(venue_id)

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')

author_ids = []

ac_ids = client.get_group(f'{venue_id}/Senior_Area_Chairs').members
ac_profiles = openreview.tools.get_profiles(client, ac_ids)

#for ac in ac_profiles:
#    count = count + 1
#    print(ac)

allowed = {}
title_id = {}
author_profiles = {}
conflicts = {}
problem_title="Collaborative Medical Triage under Uncertainty: A Multi-Agent Dynamic Matching Approach"

for note in submissions:
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in note.invitations):
        title = note.content['title']['value']
        
        try:
            area = note.content['area']['value']
            if (title == problem_title):
                print("found area")
                print(area)
            id = note.id
                            # print(area)
            allowed[title] = []
            title_id[title] = id

            if (area in area_list):
                area_acs = areas.get(area)
                for ac in ac_profiles:
                    # print(ac.id)
                    if ac.id in area_acs:
                        # print(ac.id)
                        good = True
                        for author_id in note.content['authorids']['value']:
                            if (ac.id in conflicts.keys()):
                                if (author_id in conflicts.get(ac.id)):
                                                    # print("vetoed")
                                    if (title ==  problem_title):
                                        print("vetoed")
                                    good = False
                            if (author_id in author_profiles.keys() and good):
                                conflicts_for_reviewer = openreview.tools.get_conflicts(author_profiles.get(author_id), ac)
                            elif (good):
                                author_profiles[author_id] = openreview.tools.get_profiles(client, [author_id])
                                conflicts_for_reviewer = openreview.tools.get_conflicts(author_profiles.get(author_id), ac)
                                
                            if (len(conflicts_for_reviewer) != 0 and good):
                                if ((ac.id) in conflicts.keys()):
                                    conflicts.get(ac.id).append(author_id)
                                    if (title ==  problem_title):
                                        print("vetoed")
                                    good = False
                                else:
                                    conflicts[ac.id] = []
                                    conflicts.get(ac.id).append(author_id)
                                    if (title ==  problem_title):
                                        print("vetoed")
                                    good = False
                                break
                        if good:
                            allowed[title].append(ac.id)
            else:
                # This shouldn't happen but if there are no acs for the area of this paper then check all of them
                print("WARNING")
                print(title)
                print("No ACs")
                
                        
            if (allowed[title] == []):
                print("WARNING")
                print(title)
                print("no non-conflicted ACs")
        except:
            print(title)
            print("no area")

acs = {}
assignments = {}
assignments_title_id = {}
for ac in ac_profiles:
    acs[ac.id] = 0
    assignments[ac.id] = []
    assignments_title_id[ac.id] = []
    
assigned = {}
for paper in allowed.keys():
    min_ac = 100
    min_ac_id = ""
    acs[min_ac_id] = 0
    for ac_id in allowed[paper]:
        if acs[ac_id] < min_ac:
            min_ac_id = ac_id
            min_ac = acs[ac_id]
    assigned[paper] = min_ac_id
    if (not min_ac_id == ""):
        assignments[min_ac_id].append(paper)
        assignments_title_id[min_ac_id].append(title_id[paper])

    else:
        print("WARNING")
        print(paper)
        print("No assignment")
    acs[min_ac_id] = acs[min_ac_id] + 1
    
# assignment_invitation_id = venue_group.content['senior_area_chairs_assignment_id']['value']
    
# for paper in assigned.keys():
#     print(paper)
#     print(allowed[paper])
#     print(assigned[paper])

for ac in assignments.keys():
    print(ac)
    print(assignments.get(ac))
    print(len(assignments.get(ac)))
    print(registrations.get(ac))
    print("assigned[\"" + ac + "\"] = " + str(assignments_title_id.get(ac)))
    print("\n")
    
                    
        

