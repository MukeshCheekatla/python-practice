

menu ={"pizza":3,
       "popcorn":4.5,
       "fries":2.5,
       "chips":1,
       "soda":3,
       "lemonade":4.25}

cart=[]
total=0

print("----------MENU-------------")
for key, value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("----------------------------")

while True:
    food = input("select The food: ").lower()
    if food =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-----------Your Order----------")
for food in cart:
    total += menu.get(food)
    print(food, end= " ")

print()
print(f"Total is ${total:.2f}")

