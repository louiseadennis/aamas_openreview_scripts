import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')
edit_invitation=f'{venue_id}/-/Edit'

# area_list = {'Engineering and Analysis of Multiagent Systems (EMAS)','Generative and Agentic AI (GAAI)', 'Learning and Adaptation (LEARN)', 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)', 'Game Theory and Economic Paradigms (GTEP)', 'Search, Optimization, Planning, and Scheduling (SOPS)', 'Representation and Reasoning (RR)', 'Modelling and Simluation of Societies (SIM)', 'Human-Agent Interaction (HAI)', 'Robotics and Control (ROBOT)', 'Innovative Applications (IA)'}

for note in submissions:
    #print(note.content['area']['value'])
    try:
        if note.content.get("area").get('value') == 'Innovative Applications (IA)':
            keywords = note.content.get('keywords').get('value')
            if 'IA' not in keywords:
                print('IA not in keywords')
                content = note.content
                print(content['title']['value'])
        if note.content.get("area").get('value') == 'Human-Agent Interaction (HAI)':
            keywords = note.content.get('keywords').get('value')
            if 'HAI' not in keywords:
                print('HAI not in keywords')
                content = note.content
                print(content['title']['value'])
        if note.content.get("area").get('value') == 'Modelling and Simluation of Societies (SIM)':
            keywords = note.content.get('keywords').get('value')
            if 'SIM' not in keywords:
                print('SIM not in keywords')
                content = note.content
                print(content['title']['value'])
        if note.content.get("area").get('value') == 'Representation and Reasoning (RR)':
            keywords = note.content.get('keywords').get('value')
            if 'RR' not in keywords:
                print('RR not in keywords')
                content = note.content
                print(content['title']['value'])
        if note.content.get("area").get('value') == 'Search, Optimization, Planning, and Scheduling (SOPS)':
            keywords = note.content.get('keywords').get('value')
            if 'SOPS' not in keywords:
                print('SOPS not in keywords')
                content = note.content
                print(content['title']['value'])
        if note.content.get("area").get('value') == 'Game Theory and Economic Paradigms (GTEP)':
            keywords = note.content.get('keywords').get('value')
            if 'GTEP' not in keywords:
                print('GTEP not in keywords')
                content = note.content
                print(content['title']['value'])
        if note.content.get("area").get('value') == 'Coordination, Organisations, Institutions, Norms and Ethics (COINE)':
            keywords = note.content.get('keywords').get('value')
            if 'COINE' not in keywords:
                print('COINE not in keywords')
                content = note.content
                print(content['title']['value'])
        if note.content.get("area").get('value') == 'Learning and Adaptation (LEARN)':
            keywords = note.content.get('keywords').get('value')
            if 'LEARN' not in keywords:
                print('LEARN not in keywords')
                content = note.content
                print(content['title']['value'])
        if note.content.get("area").get('value') == 'Generative and Agentic AI (GAAI)':
            keywords = note.content.get('keywords').get('value')
            if 'GAAI' not in keywords:
                print('GAAI not in keywords')
                content = note.content
                print(content['title']['value'])
        if note.content.get("area").get('value') == 'Robotics and Control (ROBOT)':
            keywords = note.content.get('keywords').get('value')
            if 'ROBOT' not in keywords:
                print('ROBOT not in keywords')
                content = note.content
                print(content['title']['value'])
        if note.content.get("area").get('value') == 'Engineering and Analysis of Multiagent Systems (EMAS)':
            keywords = note.content.get('keywords').get('value')
            if 'EMAS' not in keywords:
                print('EMAS not in keywords')
                content = note.content
                print(content['title']['value'])
    except:
        print("no area")
