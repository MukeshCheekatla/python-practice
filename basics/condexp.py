# conditional expression = A one-line shortcut for the if-else statement(ternary operator)
#                          print or assign one of the two values based on a condition
#                          x if condition else y


num= 5
a=6
b= 7
age = 25
temperature = 20
user_role="admin"

print("Postive" if num>0 else "Negative")
result = "EVEN"  if num %2 ==0 else "ODD"
max_num =a if a>b else b
min_num =a if a<b else b
status = "Adult" if age >18 else " Child"
weather = "Hot" if temperature >20 else "COLD"
access = "Success" if user_role== "admin" else " Failed"
print(access)
