import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')

learn_string = 'Learning and Adaptation (LEARN)'
gaai_string = 'Generative and Agentic AI (GAAI)'
gtep_string = 'Game Theory and Economic Paradigms (GTEP)'
coine_string = 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)'
sops_string = 'Search, Optimization, Planning, and Scheduling (SOPS)'
rr_string = 'Representation and Reasoning (RR)'
emas_string = 'Engineering and Analysis of Multiagent Systems (EMAS)'
sim_string = 'Modelling and Simluation of Societies (SIM)'
hai_string = 'Human-Agent Interaction (HAI)'
robot_string = 'Robotics and Control (ROBOT)'
ia_string = 'Innovative Applications (IA)'

learn_count = 0
gaai_count = 0
gtep_count = 0
coine_count = 0
sops_count = 0
rr_count = 0
emas_count = 0
sim_count = 0
hai_count = 0
robot_count = 0
ia_count = 0

for note in submissions:
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in note.invitations):
        if 'area' in note.content:
            if note.content['area']['value'] == learn_string:
                learn_count = learn_count + 1
            if note.content['area']['value'] == gaai_string:
                gaai_count = gaai_count + 1
            if note.content['area']['value'] == gtep_string:
                gtep_count = gtep_count + 1
            if note.content['area']['value'] == coine_string:
                coine_count = coine_count + 1
            if note.content['area']['value'] == sops_string:
                sops_count = sops_count + 1
            if note.content['area']['value'] == emas_string:
                emas_count = emas_count + 1
            if note.content['area']['value'] == sim_string:
                sim_count = sim_count + 1
            if note.content['area']['value'] == hai_string:
                hai_count = hai_count + 1
            if note.content['area']['value'] == robot_string:
                robot_count = robot_count + 1
            if note.content['area']['value'] == ia_string:
                ia_count = ia_count + 1
            if note.content['area']['value'] == rr_string:
                rr_count = rr_count + 1
  
print(learn_string + ":" + str(learn_count) + " (predicted 250 papers)")
print(gaai_string + ":" + str(gaai_count) + " (predicted 100 papers)")
print(gtep_string + ":" + str(gtep_count) + " (predicted 200 papers)")
print(coine_string + ":" + str(coine_count) + " (predicted 60 papers)")
print(sops_string + ":" + str(sops_count) + " (predicted 100 papers)")
print(rr_string + ":" + str(rr_count) + " (predicted 100 papers)")
print(emas_string + ":" + str(emas_count) + " (predicted 80 papers)")
print(sim_string + ":" + str(sim_count) + " (predicted 50 papers)")
print(hai_string + ":" + str(hai_count) + " (predicted 60 papers)")
print(robot_string + ":" + str(robot_count) + " (predicted 50 papers)")
print(ia_string + ":" + str(ia_count) + " (predicted 40 papers)")
