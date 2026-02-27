import tkinter as tk
import csv
from quiz_data import load_questions
from quiz_utility import clean_name, character_check, length_check, presence_check
from datetime import datetime

BG ="#d6eaf8"
TEXT = "#000000"
BUTTON_TEXT = "#2874a6"

questions = load_questions()


class Quizapp(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.title("GDPR Knowledge Check")
        self.questions = questions 
        self.current_questions = 0 
        self.score = 0 
        self.configure(bg=BG)
        self.geometry("600x700")
        self.name = tk.StringVar()
        self.answer_var = tk.IntVar(value=-1)
        self.answer_vars = []

        self.name_label = tk.Label(
            self,
            text="Enter your full name in the box below",
            bg=BG
            fg=TEXT
            front=("Arial", 20)
        )
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(
            self,
            textvariable=self.name,
            font=("Arial", 20),
            fg=TEXT
        )
        self.name_entry.pack(pady=10)

        self.build_question_screen()

        self.submit_button = tk.Button(
            self,
            text="Submit"
            font=("Arial", 20), 
            fg=BUTTON_TEXT,
            bg=BG
            command=self.handle_submit 
        )
        self.submit_button.pack(pady=10)

    def build_question_screen(self):

        question_number = 1

        for question in self.questions:
            q_label = tk.Label(
                self,
                text=f"Question {question_number}. {question['question']}
                font=("Arial", 20),
                wraplength=500, 
                justify="center",
                bg = BG 
            )
            q_label.pack(anchor="w", padx=40, pady=(20, 5))

            answer_var = tk.IntVar(value=-1)
            self.answer_vars.append(answer_var)

            option_value = 0 
            for option in question["options"]:
                rb = tk.Radiobutton(
                   self,
                   text=option, 
                   variable=answer_var,
                   value=option_value
                   font=("Arial", 14),
                   bg=BG 
                )
                rb.pack(anchor="w", padx=60)
                option_value += 1 
            
            question_number += 1 
        
    def hadle_submit(self): 
        
        st_name = clean_name(self.name_entry.get())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if self.validate_name_with_massage(st_name):

            answers = []
            for var in self.answer_vars:
                answers.append(var.get())
            
            with open(employee_records.csv", mode="a", newline="", encoding"utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([st_name, timestamp, answers])

            self.build_thank_you_screen(st_name)

    def build_thank_you_screen(self, name):
        self.clear_screen()

        tk.Label(
            self,
            text="Thank you for your submission, ",
            font=("Arial", 18),
            bg = BG
        ).pack(pady=20)

        tk.Label(
            self,
            text=f"{name}, the assessor will let you know your result within 5 days", 
            font=("Arial", 24),
            wraplength=500
            justify="center",
            bg = BG
            ck(pady=10)

        tk.Button(
            self,
            font=("Arial", 18),
            fg=BUTTON_TEXT, 
            bg=BG,
            text="Quit",
            command=self.destroy
        ).pack(pady=30)

    def validate_name_with_messages(self, cleaned_name: str) -> bool:
        if not presence_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Please enter your name."
            )
            valid = False

        if valid and not length_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Name must be between 2 and 50 characters."
            )
            valid = False

        if valid and not character_check(cleaned_name):
            messagebox.showerror(
                "Invalid name", 
                "Names must only contain letters, spaces, hyphens, or apostrophes."
            )
            valid = False

        return valid
    
    def clear_screen(self):

        for widget in self,winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = QuizApp(questions)
    app.mainloop()
    
    




            
             
             
            
                    
            
            
            

        



    

                








