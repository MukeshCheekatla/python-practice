
#function = A block of reusable code
#               place() after the function name to invoke it

def happy_birthday(name,age):
    print("Happpy birthday to you!")
    print("You are old!")
    print("Happy birthday to you!")
    print()

happy_birthday("rahul",22)

def display_invoice(usename, amount, due_date):
    print(f"Hello {usename}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("rahul",144,"01/01/01")



#return = statement used to end a function
#           and send a result back to the caller

def add(x,y):
    z= x+y
    return z
print(add(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first+" "+ last

print(create_name("rahul","ch"))