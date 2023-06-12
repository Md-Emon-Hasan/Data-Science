from Question import Question
question_promots = [
    "What color are Appale?\n(a) Red\n(b) Purple\n(c) Yellow\n\n",
    "What color are Banans?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_promots[0], "a"),
    Question(question_promots[1], "c"),
    Question(question_promots[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)