
#while loop = execute some code WHILE some condition remains true
#
# name = input("Enter your name: ")
#
# while name =="":
#     print("name cant be empty")
#     name = input("Enter your name")
#
# print(f"your name is {name}")
#
# food = input("Enter a food u like: ")
# while not food== "q":
#     print(f"you like {food}")
#     food = input("Enter another food: ")
#
# print("bye")
#

# num = int(input("Enter a number between 1- 10: "))
#
# while num<1 or num>10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a number between 1- 10: "))
#
# print(f"Your number is {num}")


#python compound interest calculator

principle = 0
rate = 0
time = 0

while principle<=0:
    principle =float(input("Enter an amount: "))
    if principle<=0:
        print("principal cant be less than or equal to zero")

while time<=0:
    time=float(input("Enter time "))
    if time<=0:
        print("Time cant be less than or equal to zero")

while True:
    rate=float(input("Enter interest "))
    if rate<0:
        print("Rate cant be less than or equal to zero")
    else:
        break

total = principle * pow (1+rate/100, time)

print(f"Balance after {time} year/s: ${total:.2f}")