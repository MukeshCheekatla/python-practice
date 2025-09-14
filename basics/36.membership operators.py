#Membership operators = used to test whether a value or variable is found in a sequence
#                            (string, list, tuple, set, or dictionary)
#                          1. in
#                          2. not in

string =" rahul"
for letter in string:
    print(letter, end=" ")
print()


# word ="APPLE"
#
# letter = input("Guess a letter in the secret word: ")
#
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")


# students ={"ram","sai","hui"}
#
# student = input("Enter the name of a student: ")
#
# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} was found")


grades ={"sandy":"A",
         "rahul":"A+"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student} grade is {grades[student]}")
else:
    print(f"{student} not found")



email = input("Enter your email: ")

if "@" in email and "." in email:
    print(f"{email} was valid")