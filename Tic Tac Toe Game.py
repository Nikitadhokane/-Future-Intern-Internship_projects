import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")

# Initialize the game state
current_player = "X"
game_board = [""] * 9  # List to track moves on the board

# Function to reset the game
def reset_game():
    global game_board, current_player
    current_player = "X"
    game_board = [""] * 9
    for button in buttons:
        button.config(text="", state="normal")

# Function to check for a win or draw
def check_winner():
    # Winning combinations for the Tic Tac Toe board
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in winning_combinations:
        if game_board[a] == game_board[b] == game_board[c] and game_board[a] != "":
            return game_board[a]  # Return "X" or "O" as the winner
    if "" not in game_board:
        return "Draw"  # If no empty spaces left and no winner, it's a draw
    return None  # Game is ongoing

# Function to handle button clicks
def handle_click(index):
    global current_player
    if game_board[index] == "":  # If the space is empty
        game_board[index] = current_player
        buttons[index].config(text=current_player)
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            disable_buttons()
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"

# Function to disable all buttons after game ends
def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

# Create buttons for the Tic Tac Toe grid
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, 
                       command=lambda i=i: handle_click(i))
    button.grid(row=i // 3, column=i % 3)  # Arrange in a 3x3 grid
    buttons.append(button)

# Add a reset button to restart the game
reset_button = tk.Button(root, text="Restart Game", font=("Arial", 12), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Add an exit button to close the game
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit)
exit_button.grid(row=4, column=0, columnspan=3)

# Run the application
root.mainloop()
