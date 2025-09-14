#
# friends = 25

# friends += 3
#
# friends -= 4
#
# friends *= 3
#
# friends /= 2
#
# friends **= 2
#
# friends %= 5
# print(friends)

# x = 3.14
# y = 4
# z = 5
#
# result = round(x)
# result = abs(y)
# result = pow(4,3)
# result= max(x,y,z)
# result = min(x,y,z)
# print(result)

# import math
#
# x= 10.1
#
# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)
#
# print(result)
#

import math

# radius = float(input("Enter the radius of a circle: "))
#
# circumference = 2 * math.pi * radius
#
# print(f"The cicumference is : {round(circumference,2)}")
#
# radius = float(input("Enter the radius of a circle: "))
#
# area = math.pi * pow (radius,2)
#
# print(f"The area of circle is {round(area, 2)}cm^2")
#

# import math
# a= float(input("Enter side A:"))
# b= float(input("Enter side B:"))
#
# c= math.sqrt(pow(a,2) + pow(b,2))
#
# print(f"The area of a hypotenuis traingle is {c}")


#calculator
#
# operator = input("Enter a operator(+,-,*,/,%): ")
# num1 = float(input("Enter the 1st number "))
# num2 = float(input("Enter the 2nd number "))
#
# if operator == "+":
#     result = num1 + num2
#     print(round(result))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result))
# else:
#     print(f"{operator}is not a operator")


# logical operators = evaluate multiple conditions(or, and , not)
# or = at least one condition must be true

# temp = 0
# is_raining = True
#
# if temp > 35 or temp <0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is going")

temp = 28

is_sunny = False

if temp>=28 and is_sunny:
    print("It is hot outside 🥵")
elif temp <=0 and is_sunny:
    print("It is cold ")
elif 28>temp >0 and is_sunny:
    print("It is warm outside")
elif temp>= 28 and not is_sunny:
    print("It is hot outside")
else:
    print("hush")


