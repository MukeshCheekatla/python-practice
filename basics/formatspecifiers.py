#format specifiers = {value:flags} format a value based on what
#                       flags are inserted

#. (number) f = round to that many decimal places (fixed point)
#: (number) allocate that many spaces
#:03 = allocate and zero pad that many spaces
#:<= left justify
#:> = right justify
#:^ center align
#+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
#: = insert a space before positive numbers
# :, = comma separator

price1 =3.12545
price2 =-987.85
price3 = 12.64

print(f"Price 1 is ${price1:==}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")