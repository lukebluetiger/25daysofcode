elf = 0
calories = []
input = open('day1.txt', 'r') 
lines =  input.readlines() # seperates our text file by lines

for line in lines:
    if line == "\n": # checks if the current line is empty
        calories.append(elf)
        elf = 0 # reset because we are onto a new elf
    else:
        elf += int(line)     
        
print(max(calories)) # prints the max number from the list, hence the elf with the most calories