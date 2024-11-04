import tkinter as tk
import random

# Initialize the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x300")

# Options for the game
choices = ["Rock", "Paper", "Scissors"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

# Title label
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Instruction label
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors to play:", font=("Arial", 12))
instructions_label.pack()

# Buttons for user choice
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12), command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12), command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12), command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Result display label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Reset button to play again
reset_button = tk.Button(root, text="Play Again", font=("Arial", 12), command=lambda: result_label.config(text=""))
reset_button.pack(pady=5)

# Exit button to close the game
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit)
exit_button.pack(pady=5)

# Run the application
root.mainloop()
