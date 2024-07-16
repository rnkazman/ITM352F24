# quiz.py - an interactive quiz system, fourth version
# Make QUESTIONS a dictionary, to include answer options and the correct choice.
# Allow the user to select the correct answer by its label.

QUESTIONS = {
     "What is the airspeed of an unladen swallow in miles/hr": 
     ["12", "8", "11", "15"],
     "What is the capital of Texas": 
     ["Austin", "San Antonio", "Dallas", "Waco"],
      "The Last Supper was painted by which artist": 
     ["Da Vinci", "Rembrandt", "Picasso", "Michelangelo"]
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    sorted_alternatives = sorted(alternatives)
    for label, alternative in enumerate(sorted_alternatives):
        print(f"  {label}) {alternative}")

    answer_label = int(input(f"{question}? "))
    answer = sorted_alternatives[answer_label]

    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
