# ----- Type-1: using normal python withou library
def pangrams(s):
    # Write your code here
    str = s.lower()
    word_count = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i in str:
            word_count+=1
        else:
            return "not pangram"
    return "pangram"

# ----- Type-2: using lib python
def pangrams(s):
    # Write your code here
    is_pangm = 'not pangram'
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    str = s.lower()
    for char in str:
        if char.isalpha():
            alphabet.discard(char)
        if not alphabet:
            is_pangm = 'pangram'
    return is_pangm