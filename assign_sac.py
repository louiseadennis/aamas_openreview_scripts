import openreview
import client_object
import sys

# if called with 1 as command line argument the proposed assigments will actually get posted to OpenReview
if sys.argv[1] == "1":
    print("posting")

client = client_object.client
venue_id = client_object.venue_id

registration_forum = 'vSikVyOdps' #found this id by running the get_venue_info script.


# Get all replies to the registration forum
notes = client.get_all_notes(replyto=registration_forum)

# Create a dictionary with profile_id : [subject_area]
registrations = {}
for n in notes:
    signature = n.signatures[0]
    profile = client.get_profile(signature)
    profile_id = profile.id
    if (not profile_id in registrations):
        try:
            registrations[profile_id] = n.content['area']['value']
        except:
            print(profile_id)
            print("no area")


areas = {area: sac for sac, area in registrations.items()}

acs = {}

senior_area_chairs_assignment_id = f'{venue_id}/Senior_Area_Chairs/-/Assignment'

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

        if (area in areas):
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
        else:
            # This shouldn't happen but if there are no acs for the area of this paper then assign all of them
            for ac in ac_profiles:
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
    acs[min_ac_id] = 0
    for ac_id in allowed[paper]:
        if acs[ac_id] < min_ac:
            min_ac_id = ac_id
            min_ac = acs[ac_id]
    assigned[paper] = min_ac_id
    acs[min_ac_id] = acs[min_ac_id] + 1
    
assignment_invitation_id = venue_group.content['senior_area_chairs_assignment_id']['value']
    
for paper in assigned.keys():
    print(title_id[paper])
    print(assigned[paper])
    if (sys.argv[1] == "1" and assigned[paper] != ""):
        client.post_edge(openreview.api.Edge(
        invitation=assignment_invitation_id,
        signatures=[venue_id],
        head=title_id[paper],
        tail=assigned[paper],
        weight=1,
            ))
        print("posted")
    
                    
        

