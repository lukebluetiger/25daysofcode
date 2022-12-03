score = 0
input = open('day2.txt', 'r')
lines = input.readlines()

for line in lines:
    line = list(line)
    if str(line[0]) == 'A':
      if str(line[2] == 'X'): 
        score += 1
        score += 3
      elif str(line[2] == 'Y'): 
        score += 2
        score += 6
      elif str(line[2] == 'Z'):
        score += 3
        score += 0
    elif str(line[0]) == 'B':
      if str(line[2] == 'X'): 
        score += 1
        score += 0
      elif str(line[2] == 'Y'): 
        score += 2
        score += 3
      elif str(line[2] == 'Z'):
        score += 3
        score += 6
    elif str(line[0]) == 'C':
      if str(line[2] == 'X'): 
        score += 1
        score += 6
      elif str(line[2] == 'Y'): 
        score += 2
        score += 0
      elif str(line[2] == 'Z'):
        score += 3
        score += 3

print(score)