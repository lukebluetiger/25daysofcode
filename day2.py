score = 0
input = open('day2.txt', 'r')
lines = input.readlines()
scores = {"X": 1, "Y": 2, "Z": 3}  # an index dict of our scores
matches = {  # a dict for our possible matches and scores for those
    "A X": 3,
    "B Y": 3,
    "C Z": 3,
    "A Y": 6,
    "B Z": 6,
    "C X": 6,
    "A Z": 0,
    "B X": 0,
    "C Y": 0
}
new_scores = {  # for our part 2, with the official guide we learn what the scores for the matches actually mean
    "A X": 3,
    "B X": 1,
    "C X": 2,
    "B Y": 2,
    "A Y": 1,
    "C Y": 3,
    "C Z": 1,
    "B Z": 3,
    "A Z": 2
}
outcome = {  # now we know these are outcome scores
    "Y": 3,
    "X": 0,
    "Z": 6
}

for line in lines:
    line = list(line)  # turn our line into a list
    # add the intial score of whatever were playing
    score += scores[str(line[2])]
    # add the match score based on the match
    score += matches[''.join(map(str, line[:3]))]

print(score)

score = 0  # reset it to 0 before starting part 2

for line in lines:
    # add the new match scores
    score += new_scores[''.join(map(str, line[:3]))]
    score += outcome[str(line[2])]  # add the outcome scores

print(score)
