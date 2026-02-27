import csv
import os

def load_questions(filepath="quiz_questions.csv"):
    if filepath is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, 'quiz_questions.csv')
    
    questions = []

    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions.append({
                "question": row["question"],
                "options": [
                    row["option_a"], 
                    row["option_b"],
                    row["option_c"],
                    row["option_d"],
                ],
                "correct": int(row["correct"]) - 1 
            })

    return questions