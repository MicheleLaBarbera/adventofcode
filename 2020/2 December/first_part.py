input_file = open('input.txt', 'r') 
policies = input_file.readlines() 
  
count = 0
for policy in policies: 
  splitted_policy = policy.split(' ')
  splitted_min_max = splitted_policy[0].split('-')

  min_count = int(splitted_min_max[0])
  max_count = int(splitted_min_max[1])

  char_check = splitted_policy[1][:-1]

  password = splitted_policy[2]

  occurrences = 0
  for i in range(0, len(password)):
    if(password[i] == char_check):
      occurrences += 1

  if(min_count <= occurrences <= max_count):
    count += 1

print("Valid passwords count: " + str(count))
    