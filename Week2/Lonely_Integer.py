# ----- Type-1: using plain python function ------
def lonelyinteger(a):
    # Write your code here
    not_unique = False
    for item in range(len(a)):
        # This checks if a[i] appears in the sublist that starts immediately after a[i].
        if a[item] in a[item + 1:]:
            not_unique = False
        # This checks if a[i] appears in the sublist that ends immediately before a[i].
        elif a[item] in a[:item]:
            not_unique = False
        else:
            not_unique = True
            return a[item]

# ----- Type-2: using count() function ------
def lonelyinteger(a):
    # Write your code here
    for item in a:
        if a.count(item) == 1:
            return item

# ----- Type-3: using XOR operator function ------
def lonelyinteger(a):
    original_number = 0
    # Iterate through each element in the array
    for item in a:
        # Use XOR operation to find the unique element
        original_number ^= item

    # Return the unique element
    return original_number
"""
    Explanation:
       XOR properties: 
        - Identity: a⊕0 = a
        - Self-Cancellation: a⊕a =0
        - Commutative: a⊕b = b⊕a
        - Associative: a⊕(b⊕c) = (a⊕b)⊕c

       Let's denote the array as [x1,x2,...,xn] where every element xi appears exactly twice except for one unique element u.
       Let's denote the XOR operation applied to all elements of the array as R.
       R=x1⊕x2⊕...⊕xn
       
       According the properties of XOR, we can group the elements that appear twice and simplify:
       R = (a⊕a)⊕(b⊕b) ⊕(u)
       
       Here, XORing all elements in the array will cancel out all duplicate elements leaving us with the unique element u.
"""