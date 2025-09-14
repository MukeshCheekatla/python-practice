#Match-case statement (switch): An alternative to using many 'elif' statements
#                               Execute some code if a value matches a case
#                               Benefits: cleaner and syntax is more readable
from typing import reveal_type


def day_of_week(day):
    match day:
        case 1 | 8 | 13:
            return "MONDAY"
        case 2:
            return "TUESDAY"
        case 3:
            return "WEDNESDAY"
        case 4:
            return "THURSDAY"
        case 5:
            return "FRIDAY"
        case 6:
            return "SATURDAY"
        case 7:
            return "SUNDAY"
        case _:
            return "Not a valid day"

print(day_of_week(int(input("Enter a day: "))))






