# *args  = allows you to pass multiple non-key arguments
#**kwargs = allows you to pass multiple keyword-arguments
#           unpacking operator
#           1. positional   2. default 3. keyword   4. ARBITRARY

# def add(*args):
#     total=0
#     for arg in args:
#         total +=arg
#
#     return total
#
# print(add(1,2,3,4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Mr.", "rahul")


# def print_address(**kwargs):
#     for key,values in kwargs.items():
#         print(f" {key:10} :{values}")
#
# print_address(street="bt", city="amp", state="Ap", zip=533222)


def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    print(f"{kwargs.get('street')} {kwargs.get(('apt'))}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('country')}")

shipping_label("Mr.", "Rahul",
               street="bt",
               apt="8-65",
               city="Amp",
               state="Ap",
               Country="India"
               )
