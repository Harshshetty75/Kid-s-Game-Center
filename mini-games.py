import tkinter as tk
from tkinter import messagebox
import random

# Guess the Number Game
def guess_the_number_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    def check_guess():
        nonlocal attempts
        attempts += 1
        guess = int(guess_entry.get())

        if guess < secret_number:
            result_label.config(text="Too low. Try again.")
        elif guess > secret_number:
            result_label.config(text="Too high. Try again.")
        else:
            result_label.config(text=f"Congratulations! You guessed the number in {attempts} attempts.")
            play_again_button.pack()
            guess_button.config(state=tk.DISABLED)

    root = tk.Toplevel()
    root.title("Guess the Number Game")
    root.configure(background="white")

    instructions_label = tk.Label(root, text="I'm thinking of a number between 1 and 100.\nCan you guess it?",
                                  fg="black", bg="white", font=("Arial", 12))
    instructions_label.pack(pady=10)

    guess_entry = tk.Entry(root)
    guess_entry.pack()

    guess_button = tk.Button(root, text="Guess", command=check_guess, bg="orange", fg="white", padx=10, pady=5,
                             font=("Arial", 12))
    guess_button.pack(pady=5)

    result_label = tk.Label(root, text="", fg="black", bg="white", font=("Arial", 12))
    result_label.pack(pady=10)

    def play_again():
        nonlocal secret_number, attempts
        secret_number = random.randint(1, 100)
        attempts = 0
        result_label.config(text="")
        guess_button.config(state=tk.NORMAL)
        play_again_button.pack_forget()

    play_again_button = tk.Button(root, text="Play Again", command=play_again, bg="orange", fg="white", padx=10, pady=5,
                                  font=("Arial", 12))
    play_again_button.pack()

# Word Scramble Game
def word_scramble_game():
    words = ["PYTHON", "PROGRAMMING", "JUPYTER", "NOTEBOOK", "HANGMAN", "GAME"]
    word = random.choice(words)

    def scramble_word():
        scrambled_word = "".join(random.sample(word, len(word)))
        word_label.config(text=scrambled_word)

    def check_answer():
        user_answer = answer_entry.get().upper()

        if user_answer == word:
            result_label.config(text="Correct! You guessed the word.")
        else:
            result_label.config(text="Incorrect. Try again.")

    root = tk.Toplevel()
    root.title("Word Scramble Game")
    root.configure(background="white")

    word_label = tk.Label(root, text="", font=("Arial", 20), fg="black", bg="white")
    word_label.pack(pady=10)

    scramble_word()

    answer_entry = tk.Entry(root)
    answer_entry.pack()

    check_button = tk.Button(root, text="Check", command=check_answer, bg="blue", fg="white", padx=10, pady=5,
                             font=("Arial", 12))
    check_button.pack(pady=5)

    result_label = tk.Label(root, text="", fg="black", bg="white", font=("Arial", 12))
    result_label.pack(pady=10)

    play_again_button = tk.Button(root, text="Play Again", command=lambda: [scramble_word(), result_label.config(text="")],
                                  bg="blue", fg="white", padx=10, pady=5, font=("Arial", 12))
    play_again_button.pack()

# Rock-Paper-Scissors Game
def rock_paper_scissors_game():
    choices = ["Rock", "Paper", "Scissors"]

    def get_computer_choice():
        return random.choice(choices)

    def play(choice):
        computer_choice = get_computer_choice()
        result_label.config(text=f"Computer chose: {computer_choice}")

        if choice == computer_choice:
            result_label.config(text="It's a tie!")
        elif (
            (choice == "Rock" and computer_choice == "Scissors")
            or (choice == "Paper" and computer_choice == "Rock")
            or (choice == "Scissors" and computer_choice == "Paper")
        ):
            result_label.config(text="You win!")
        else:
            result_label.config(text="You lose!")

    root = tk.Toplevel()
    root.title("Rock-Paper-Scissors Game")
    root.configure(background="white")

    rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"), bg="red", fg="white", padx=10, pady=5,
                            font=("Arial", 12))
    rock_button.pack(side=tk.LEFT, padx=10)

    paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"), bg="green", fg="white", padx=10, pady=5,
                             font=("Arial", 12))
    paper_button.pack(side=tk.LEFT, padx=10)

    scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"), bg="yellow", fg="black",
                                padx=10, pady=5, font=("Arial", 12))
    scissors_button.pack(side=tk.LEFT, padx=10)

    result_label = tk.Label(root, text="", fg="black", bg="white", font=("Arial", 12))
    result_label.pack(pady=10)

# Hangman Game
def hangman_game():
    words = ["PYTHON", "PROGRAMMING", "JUPYTER", "NOTEBOOK", "HANGMAN", "GAME"]
    word = random.choice(words).upper()
    guessed_letters = set()
    attempts = 6

    def update_display():
        display_word = "".join(letter if letter in guessed_letters else "-" for letter in word)
        word_label.config(text=display_word)

    def on_letter_click(letter):
        nonlocal attempts
        guessed_letters.add(letter)
        if letter not in word:
            attempts -= 1
            if attempts == 0:
                messagebox.showinfo("Game Over", "You lost! The word was: " + word)
                root.quit()
        else:
            update_display()
            if "-" not in word_label.cget("text"):
                messagebox.showinfo("Congratulations", "You win! You guessed the word.")
                root.quit()

    root = tk.Toplevel()
    root.title("Hangman Game")
    root.configure(background="white")

    word_label = tk.Label(root, text="", font=("Arial", 20), fg="black", bg="white")
    word_label.pack(pady=10)

    letters_frame = tk.Frame(root)
    letters_frame.pack()

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letter_btn = tk.Button(letters_frame, text=letter, command=lambda l=letter: on_letter_click(l), bg="purple",
                               fg="white", padx=10, pady=5, font=("Arial", 12))
        letter_btn.grid(row=(ord(letter) - ord("A")) // 6, column=(ord(letter) - ord("A")) % 6)

    update_display()

# Main Game Selection Menu
def game_center():
    root = tk.Tk()
    root.title("Kids' Game Center")
    root.configure(background="white")

    title_label = tk.Label(root, text="Welcome to the Kids' Game Center!", font=("Arial", 16), fg="black", bg="white")
    title_label.pack(pady=10)

    game_options = [
        ("Guess the Number", guess_the_number_game),
        ("Word Scramble", word_scramble_game),
        ("Rock-Paper-Scissors", rock_paper_scissors_game),
        ("Hangman", hangman_game)
    ]

    for game, func in game_options:
        game_button = tk.Button(root, text=game, command=func, bg="purple", fg="white", padx=10, pady=5, font=("Arial", 12))
        game_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    game_center()
