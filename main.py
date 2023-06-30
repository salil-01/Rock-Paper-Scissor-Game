import random
import tkinter as tk
from tkinter import messagebox

player_score = 0
computer_score = 0
player_score_display = None
computer_score_display = None

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'Tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'scissors' and computer_choice == 'paper') or \
            (player_choice == 'paper' and computer_choice == 'rock'):
        return 'Player'
    else:
        return 'Computer'

def play_round(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    winner = determine_winner(player_choice, computer_choice)

    if winner == 'Player':
        return 'Player', computer_choice
    elif winner == 'Computer':
        return 'Computer', computer_choice
    else:
        return 'Tie', computer_choice

def update_score(result):
    global player_score, computer_score
    if result == 'Player':
        player_score += 1
    elif result == 'Computer':
        computer_score += 1

def reset_scores():
    global player_score, computer_score, player_score_display, computer_score_display
    player_score = 0
    computer_score = 0
    player_score_display.config(text=player_score)
    computer_score_display.config(text=computer_score)

def play_game():
    def on_choice_selected(choice):
        result, comp_choice = play_round(choice)
        update_score(result)
        computer_choice.set(comp_choice)
        if result == 'Tie':
            messagebox.showinfo("Result", f"Computer chooses: {computer_choice.get()}\n\nIt's a tie!")
        else:
            messagebox.showinfo("Result", f"Computer chooses: {computer_choice.get()}\n\n{result} wins this round!")
        player_score_display.config(text=player_score)
        computer_score_display.config(text=computer_score)

    def end_game():
        messagebox.showinfo("Game Over", f"Final Score:\nPlayer: {player_score}\nComputer: {computer_score}")
        reset_scores()
        window.quit()

    global player_score_display, computer_score_display
    window = tk.Tk()
    window.title("Rock-Paper-Scissors")
    window.geometry("300x200")

    computer_choice = tk.StringVar()

    score_label = tk.Label(window, text="Score", font=("Arial", 12, "bold"))
    score_label.pack(pady=10)

    score_frame = tk.Frame(window)
    score_frame.pack()

    player_score_label = tk.Label(score_frame, text="Player:", font=("Arial", 10))
    player_score_label.pack(side=tk.LEFT)
    player_score_display = tk.Label(score_frame, text=player_score, font=("Arial", 10, "bold"))
    player_score_display.pack(side=tk.LEFT, padx=5)

    computer_score_label = tk.Label(score_frame, text="Computer:", font=("Arial", 10))
    computer_score_label.pack(side=tk.LEFT)
    computer_score_display = tk.Label(score_frame, text=computer_score, font=("Arial", 10, "bold"))
    computer_score_display.pack(side=tk.LEFT, padx=5)

    choices_frame = tk.Frame(window)
    choices_frame.pack(pady=10)

    rock_button = tk.Button(choices_frame, text="Rock", width=10, command=lambda: on_choice_selected("rock"))
    rock_button.pack(side=tk.LEFT, padx=5)
    paper_button = tk.Button(choices_frame, text="Paper", width=10, command=lambda: on_choice_selected("paper"))
    paper_button.pack(side=tk.LEFT, padx=5)
    scissors_button = tk.Button(choices_frame, text="Scissors", width=10, command=lambda: on_choice_selected("scissors"))
    scissors_button.pack(side=tk.LEFT, padx=5)

    quit_button = tk.Button(window, text="Quit", width=10, command=end_game)
    quit_button.pack(pady=10)

    window.mainloop()

# Start the game
play_game()
