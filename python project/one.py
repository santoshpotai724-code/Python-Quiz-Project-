
import random

quetions = [
    ("Which function is used to display output in Python?",
     ("A.input()", "B.display()", "C.print()", "D.show()"), "C"),

    ("Which symbol is used for comments in Python?",
     ("A.//", "B.#", "C/* */", "D.@"), "B"),

    ("What is the output of print(5 + 3)?",
     ("A.6", "B.5", "C.8", "D.7"), "C"),

    ("Which data type stores True or False values?",
     ("A.float", "B.bool", "C.int", "D.complex"), "B"),

    ("Which loop is used to repeat code while a condition is true?",
     ("A.while", "B.for", "C.do-while", "D.def"), "A"),

    ("Which of the following are valid Python data types?",
     ("A.str", "B.number", "C.float", "D.int"), "A"),

    ("Which keyword is used to define a function in Python?",
     ("A.function", "B.def", "C.fun", "D.define"), "B"),

    ("Which operator is used for exponentiation in Python?",
     ("A.*", "B.//", "C.**", "D.%"), "C"),

    ("Which function is used to find the length of a list?",
     ("A.count()", "B.size()", "C.len()", "D.length()"), "C"),

    ("Which keyword is used to stop a loop?",
     ("A.stop", "B.exit", "C.break", "D.continue"), "C")
]

random.shuffle(quetions)

score = 0

for quetion, option, answer in quetions:

    print("--------------------")
    print(quetion)

    for opt in option:
        print(opt)

    # Input validation
    while True:
        guse = input("Enter A, B, C, D: ").strip().upper()

        if guse in ("A", "B", "C", "D"):
            break
        else:
            print("Invalid option! Please enter A, B, C or D.")

    if guse == answer:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answer} is the correct answer")

print("****************************")
print("         RESULT             ")
print("****************************")

score_percent = (score / len(quetions)) * 100

print(f"Your score: {score}/{len(quetions)}")
print(f"Your percentage: {score_percent:.2f}%")

if score_percent > 60:
    print("Result: Pass")
else:
    print("Result: Fail")
