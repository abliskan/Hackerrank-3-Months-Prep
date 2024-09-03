# ----- Type-1: 1 line python function
def flippingBits(n):
    # Write your code here
    return n ^ 2**32-1

# ----- Type-2: using .format() build-in python
def flippingBits(n):
    var_int = ''
    bit_convert = format(n, '032b')
    for i in bit_convert:
       if i == '1':
         var_int += '0'
       else:
         var_int += '1'
         
    return int(var_int, 2)