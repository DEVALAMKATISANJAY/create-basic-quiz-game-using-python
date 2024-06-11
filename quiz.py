quiz = [{'question': "What is the capital of India?",
         'options': ["A) Bangalore", "B) Delhi", "C) Mumbai", "D) Hyderabad"],
         'answer': "B"},
        {'question': "Who is the PM of India?",
         'options': ["A) Narendra Modi", "B) Manmohan Singh", "C) Sardar", "D) Rahul Gandhi"],
         'answer': "A"},
        {'question': "What is 3 + 2?",
         'options': ["A) 3", "B) 4", "C) 5", "D) 6"],
         'answer': "C"},
        {'question': "What is the factorial of 5?",
         'options':["A) 80", "B) 120", "C) 60", "D) 40"],
         'answer':"B"}]
def run_quiz(quiz):
    score = 0
    total_questions = len(quiz)
    for q in quiz:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['answer']}.")
        print()
    print(f"\nYour score is {score} out of {total_questions} questions.")
    if score == total_questions:
        print("Excellent! You got all the answers right!")
    elif score >= total_questions / 2:
        print("Good job! You did well.")
    else:
        print("Better luck next time. Keep practicing!")
run_quiz(quiz)