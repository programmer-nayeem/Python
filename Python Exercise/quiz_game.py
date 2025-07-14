# Python Quiz Game

questions = (
    "What is the capital of France?",
    "What is 2 + 2?",
    "What is the largest planet in our solar system?",
    "What is the boiling point of water in Celsius?",
    "What is the chemical symbol for gold?"
)

options = (
    ("A) Paris", "B) London", "C) Berlin", "D) Madrid"),
    ("A) 3", "B) 4", "C) 5", "D) 6"),
    ("A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"),
    ("A) 90", "B) 100", "C) 110", "D) 120"),
    ("A) Au", "B) Ag", "C) Pb", "D) Hg")
)

answers = ("A", "B", "C", "B", "A")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[questions_num]:
        print(option)

    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[questions_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer was: {answers[questions_num]}")

    questions_num += 1

print("---------------------")
print("Quiz complete!")
print(f"Your score: {score}/{len(questions)}")