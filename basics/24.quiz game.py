
# python quiz game

questions =( "What is the output of print(2 ** 3)?",
    "Which of the following is a mutable data type in Python?",
    "What keyword is used to define a function in Python?",
    "Which operator is used for floor division in Python?",
    "What is the correct file extension for Python files?")

options = (("A. 6", "B. 8", "C. 9", "D. 12"),
    ("A. tuple", "B. string", "C. list", "D. int"),
    ("A. func", "B. def", "C. function", "D. lambda"),
    ("A. /", "B. //", "C. %", "D. **"),
    ("A. .pyt", "B. .py", "C. .pt", "D. .python"))

answers = ("B", "C", "B", "B", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")


    question_num +=1

print("-----------------------")
print("       RESULTS         ")
print("-----------------------")

print("answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score/len(questions)*100)
print(f"Your score is {score}%")