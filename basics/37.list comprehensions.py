#List comprehension = A concise way to create lists in Python
#                   Compact and easier to read than traditional loops
#                   [expression for value in iterable if condition]


# doubles = []
# for x in range(1,11):
#     doubles.append(x)


#         [expression for value in iterable if condition]
# doubles = [    x*2    for   x   in  range(1,11)]
# squares = [z*z for z in range(1,100)]
#
# print(squares)

#
# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]

# fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
# fruit_chart = [fruit[0] for fruit in fruits]
#
# print(fruit_chart)

#
# numbers = [-1, -2, -3, -4,1,2,5,9]
# positive_nums = [num for num in numbers if num>=0]
# negative_nums = [num for num in numbers if num<0]
# even_nums =[num for num in numbers if num%2 ==0]
#
# print(positive_nums)
# print(negative_nums)
# print(even_nums)



grades =[85,90,87,65,54]
passing_grades=[grade for grade in grades if grade>=60]

print(passing_grades)