import csv

filename = 'subject_scores.csv'

assignments = {}
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] in assignments.keys():
            assignments.get(row[0]).append(row[1])
        else:
            assignments[row[0]] = [row[1]]
        
for key in assignments.keys():
    print("assigned[\"" + key + "\"] = " + str(assignments.get(key)))
