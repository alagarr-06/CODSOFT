import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x350")
        self.root.configure(bg="#f2f4f7")

        self.user_score = 0
        self.computer_score = 0

        tk.Label(
            root,
            text="Rock Paper Scissors",
            font=("Arial", 16, "bold"),
            bg="#f2f4f7"
        ).pack(pady=10)

        self.result_label = tk.Label(
            root,
            text="Choose your move",
            font=("Arial", 12),
            bg="#f2f4f7"
        )
        self.result_label.pack(pady=5)

        btn_frame = tk.Frame(root, bg="#f2f4f7")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Rock", width=10, command=lambda: self.play("Rock")).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Paper", width=10, command=lambda: self.play("Paper")).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Scissors", width=10, command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=5)

        self.score_label = tk.Label(
            root,
            text="You: 0  |  Computer: 0",
            font=("Arial", 12, "bold"),
            bg="#f2f4f7"
        )
        self.score_label.pack(pady=10)

        tk.Button(
            root,
            text="Reset Score",
            width=20,
            bg="#f44336",
            fg="white",
            command=self.reset_score
        ).pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "Computer Wins!"
            self.computer_score += 1

        self.result_label.config(
            text=f"You chose {user_choice}, Computer chose {computer_choice}\n{result}"
        )
        self.update_score()

    def update_score(self):
        self.score_label.config(
            text=f"You: {self.user_score}  |  Computer: {self.computer_score}"
        )

    def reset_score(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="Choose your move")
        self.update_score()

root = tk.Tk()
app = RockPaperScissors(root)
root.mainloop()
