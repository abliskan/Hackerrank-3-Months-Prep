# ----- Type-1: use data from path only

def countingValleys(steps, path):
    """ rule:
    - sea level start from 0
    - once hiker enter a valley (uppper or below sea level) we add +1 to vally count,
    - after hiker is step down the sea level is decrease,
    - hiker definitely needs to reach the sea level back to 0, after some steps later
    
        code flow:
    - we increment and decrement the sea_level base on path,
    - when sea_level reaches 0 -> we check if the last step was U -> [True] we just finished a valley (so increase the count_valleys + 1)
    """
    sea_level, count_valleys = 0, 0
    # Iterate through each step in the path
    for i in path:
        # If the step is an 'U', move up; otherwise, move down
        if i == 'U':
            sea_level += 1
        else:
            sea_level -= 1

        # Check if the current level is 0 and the step is an 'U', indicating we're back at sea level after descending
        if sea_level == 0 and i == 'U':
            # Increment the valleys count
            count_valleys += 1

    # Return the total number of valleys encountered
    return count_valleys

# ----- Type-2: use data from path and step argument
def countingValleys(steps, path):
    i, sea_level, count_valleys, last_step = 0, 0, 0, ''
    while i < steps:
        if path[i] == 'U':
            sea_level += 1
            last_step = "U"
        else:
            sea_level -= 1
            last_step = "D"
						
        if sea_level == 0 and last_step == "U":
            count_valleys += 1
        i += 1
        
    return count_valleys

# ----- Type-3: 
