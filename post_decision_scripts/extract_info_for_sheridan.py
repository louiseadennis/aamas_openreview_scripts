import openreview
import client_object
from utils import SubmissionSet

client = client_object.client

year = "2026"

submission_date = "8-OCT-2025"
decision_date = "22-DEC-2025"


venue_id = client_object.venue_id
client.impersonate(venue_id)

reply_type = "Decision"
submissions = SubmissionSet(client,venue_id,True)

# set submission filters
# decisions: full, ea, reject
decision_set = ["full"]

# tracks: "LEARN", "GTEP", "COINE", "SOPS", "RPR", "EMAS", "SIM", "HAI", "ROBOT", "IA"
track_set = []

# only process submissions with scores above a threshold
score_threshold = 0

# filter by a set of submission ids
submission_set = []

# supported: csv or xml
#output_format = "csv"
output_format = "xml"

'''
*** csv only options (short or long): *** 
'''

# print author emails in addition to names
author_print_format = "long"

# print submissions in the specified format
submissions.printPapers(output_format,year,submission_set,author_print_format,
                        decision_set,track_set,score_threshold,
                        submission_date,decision_date)

# print submission counts by track
#submissions.printCounts(track_set)

# print length of reviews by track
#submissions.printReviewLength(track_set)

# print average scores by track
#submissions.printAverageScores(track_set)
