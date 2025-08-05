import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id



areas = {}
areas['Modelling and Simluation of Societies (SIM)'] = ['~Louise_Sellers1']
areas['Robotics and Control (ROBOT)'] = ['~Rafael_C._Cardoso1','~Mengwei_Xu1','~Louise_Sellers1']
areas['Engineering and Analysis of Multiagent Systems (EMAS)'] = ['~Rafael_C._Cardoso1','~Louise_Sellers1']
areas['Generative and Agenti AI (GAAI)'] = ['~Mengwei_Xu1','~Rafael_C._Cardoso1']
areas['Learning and Adaptation (LEARN)'] = ['~Louise_A._Dennis1']

acs = {}

venue_id = 'AAMAS/2026/Test'
senior_area_chairs_proposed_assignment_id = 'AAMAS/2026/Test/Senior_Area_Chairs/-/Proposed_Assignment'

venue_group = client.get_group(venue_id)

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')

author_ids = []

ac_ids = client.get_group(f'{venue_id}/Senior_Area_Chairs').members
ac_profiles = openreview.tools.get_profiles(client, ac_ids)

allowed = {}
title_id = {}

for note in submissions:
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in note.invitations):
        title = note.content['title']['value']
        area = note.content['area']['value']
        id = note.id
        print(area)
        allowed[title] = []
        title_id[title] = id

        for ac in ac_profiles:
            if ac.id in areas[area]:
                good = True
                for author_id in note.content['authorids']['value']:
                    conflicts_for_reviewer = openreview.tools.get_conflicts(openreview.tools.get_profiles(client, [author_id]), ac)
                    if len(conflicts_for_reviewer) != 0:
                        good = False
                        break
                if good:
                    allowed[title].append(ac.id)

acs = {}
for ac in ac_profiles:
    acs[ac.id] = 0
    
assigned = {}
for paper in allowed.keys():
    min_ac = 100
    min_ac_id = ""
    for ac_id in allowed[paper]:
        if acs[ac_id] < min_ac:
            min_ac_id = ac_id
            min_ac = acs[ac_id]
    assigned[paper] = min_ac_id
    acs[min_ac_id] = acs[min_ac_id] + 1
    
assignment_invitation_id = venue_group.content['senior_area_chairs_assignment_id']['value']
    
for paper in assigned.keys():
    client.post_edge(openreview.api.Edge(
        invitation=senior_area_chairs_proposed_assignment_id,
        signatures=[venue_id],
        head=title_id[paper],
        tail=assigned[paper],
        weight=1,
    ))
    
                    
        

