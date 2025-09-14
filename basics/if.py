


# age = int(input("enter your age: "))
#
# if age>= 18:
#     print("You are now signed")
# elif age <0:
#     print("are you rally born")
# else:
#     print("you are not old enough")

#
# response = input("would you like food? (Y/N)")
#
# if response == "Y":
#     print("have some food")
# else:
#     print("no food")


# online = True
# if online:
#     print("User is online")
# else:
#     print("not online")


#
# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or pounds? (K or L): ")
#
# if unit == "K":
#     weight = weight*2.205
#     unit = "Lbs"
#     print(f"Your weight is {round(weight,2)}{unit}")
# elif unit == "L":
#     weight = weight/2.205
#     unit = "Kgs"
#     print(f"Your weight is {weight}{unit}")
# else:
#     print(f"{unit} was not valid")


unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round ((9*temp)/ 5+32,1)
    print(f"The temperature in Fahrenheit is : {temp}°F")
elif unit == "F":
    temp = round ((temp - 32) *5/9,1)
    print(f"The temperature in celcius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")

