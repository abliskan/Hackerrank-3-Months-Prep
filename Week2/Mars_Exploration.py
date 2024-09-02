# ----- Type-1: check string one by one in loop
def marsExploration(s):
    # Write your code here
    transmission_change = 0
    signal_pattern = ['S', 'O', 'S']
    for i in range(len(s)):
        mod_cal = i % 3
        signal_char = s[i]
        if signal_char != signal_pattern[mod_cal]:
            transmission_change += 1
    return transmission_change

# ----- Type-2: check string per 3 index
def marsExploration(s):
    # Write your code here
    transmission_change = 0
    for i in range(0, len(s), 3):
        if s[i] != 'S':
            transmission_change += 1
        if s[i + 1] != 'O':
            transmission_change += 1
        if s[i + 2] != 'S':
            transmission_change += 1
    return transmission_change