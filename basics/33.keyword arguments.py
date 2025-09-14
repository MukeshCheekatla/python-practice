
#keyword arguments = an argument precede by an identifier
#                            helps with readability
#                           order of arguments doesn't matter
#                    1. positional 2. default 3. KEYWORD 4. arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")
#
# hello("hello", title="hi",  last="ch",  first="rahul")

# for x in range(1,11):
#     print(x,end=" ")
#
# print("1","2","3","4",sep=" - ")

def get_phone(country, area, first, last):
     return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(91, area=8688, first=392, last=919)
print(phone_num)










