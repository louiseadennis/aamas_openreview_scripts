import openreview
import client_object

client = client_object.client
venue_id = client_object.venue_id

venue_group = client.get_group(venue_id)

r_ids = client.get_group(f'{venue_id}/Reviewers').members
r_profiles = openreview.tools.get_profiles(client, r_ids)

assignment_id = f'{venue_id}/Reviewers/-/Assignment'
#assignment_invitation_id = venue_group.content['assignment_id']['value']
grouped_edges = client.get_grouped_edges(
    invitation = assignment_id,
    groupby = 'tail')
    
submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission')

rev_assignment_map = {group['id']['tail']:group['values'] for group in grouped_edges}

count = 0
rev = "~Gian_Luca_Scoccia1"
#for rev in r_ids:
print(rev_assignment_map.get(rev))
print(len(rev_assignment_map.get(rev)))
print(count)

