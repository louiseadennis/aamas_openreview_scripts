import sys

ideal_load = int(sys.argv[1])
max_load = int(sys.argv[2])
reduced_reviewers = int(sys.argv[3])
their_load = int(sys.argv[4])
num_reviewers = int(sys.argv[5])

normal_reviewers = num_reviewers - reduced_reviewers

ideal_normal = ideal_load * normal_reviewers
max_normal = max_load * normal_reviewers

total_ideal = ideal_normal + their_load
total_max = max_normal + their_load



print("Ideal capacity is " + str(total_ideal/3))
print("Max capacity is " + str(total_max/3))
