# quiz.py - an interactive quiz system, fifth version
# - Make QUESTIONS a dictionary, to include answer options and the correct choice.
# - Allow the user to select the correct answer by its label.
# - Improve the look and usability.  Keep track of correct answers.

from string import ascii_lowercase

QUESTIONS = {
     "What is the airspeed of an unladen swallow in miles/hr": 
     ["12", "8", "11", "15"],
     "What is the capital of Texas": 
     ["Austin", "San Antonio", "Dallas", "Waco"],
      "The Last Supper was painted by which artist": 
     ["Da Vinci", "Rembrandt", "Picasso", "Michelangelo"]
}

num_correct = 0
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct_answer = alternatives[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    answer_label = input("\nChoice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        num_correct += 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")
