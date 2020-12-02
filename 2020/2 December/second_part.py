input_file = open('input.txt', 'r') 
policies = input_file.readlines() 
  
count = 0
for policy in policies: 
  splitted_policy = policy.split(' ')
  splitted_min_max = splitted_policy[0].split('-')

  min_count = int(splitted_min_max[0]) - 1
  max_count = int(splitted_min_max[1]) - 1

  char_check = splitted_policy[1][:-1]

  password = splitted_policy[2].strip()

  if((password[min_count] == char_check) ^ (password[max_count] == char_check)):
    count += 1

print("Valid passwords count: " + str(count))
    