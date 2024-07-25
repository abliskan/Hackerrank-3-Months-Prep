# ----- Type-1 ------
def breakingRecords(scores):
    # Write your code here
    result = [0, 0]
    minimum, maximum = scores[0], scores[0]
    for element in scores[1:]:
        if element < minimum:
            minimum = element
            result[1] += 1
        elif element > maximum:
            maximum = element
            result[0] += 1
    return result

# ----- Type-2 ------
def breakingRecords(scores):
    mincount = maxcount = 0
    minscore = maxscore = scores[0]
    
    for i in range(1, len(scores)):
        if minscore < scores[i]:
           minscore = scores[i]
           mincount += 1
        elif maxscore > scores[i]:
           maxscore = scores[i]
           maxcount += 1
    return mincount, maxcount       

# ----- Type-3 ------
def breakingRecords(scores):
    minimum = 0
    maximum = 0
    for index, value in enumerate(scores):
        if index == 0: 
            continue
        if value < min(scores[: index]):
            minimum += 1
        if value > max(scores[: index]):
            maximum += 1
    return [maximum, minimum]