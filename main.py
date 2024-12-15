import tkinter as tk
import random
import os, sys

# Ustawienie ikony gry (plik game_icon.ico musi być w tym samym katalogu)
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
icon_path = os.path.join(base_path, "game_icon.ico")

# Funkcja do rozpoczecia nowej gry
def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 10)
    attempts = 0
    result_label.config(text=f"Guess a number between 1 and 10! You have {max_attempts} attempts.")
    guess_entry.config(state=tk.NORMAL)

    # Czyszczenie pola wejściowego przy rozpoczęciu nowej gry
    guess_entry.delete(0, tk.END)

# Funkcja do sprawdzenia zgadywanej liczby
          def check_guess(event=None):  # Dodajemy event, by obsłużyć zdarzenie Enter
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1

        if guess < secret_number:
            result_label.config(text="Too low! Try again.")
        elif guess > secret_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"Congratulations! You guessed it in {attempts} attempts!")
            guess_entry.config(state=tk.DISABLED)

        # Sprawdzenie, czy gracz przekroczyl liczbe prob
        if attempts >= max_attempts and guess != secret_number:
            result_label.config(text=f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}")
            guess_entry.config(state=tk.DISABLED)

        # Czyszczenie pola wejściowego po naciśnięciu Enter
        guess_entry.delete(0, tk.END)

    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

# Tworzenie glównego okna
window = tk.Tk()
window.title("Guessing Game")
window.iconbitmap(icon_path)

# Etykiety
welcome_label = tk.Label(window, text="Welcome to the guessing game!", font=("Arial", 14))
welcome_label.pack(pady=10)

result_label = tk.Label(window, text="I have chosen a number between 1 and 10. Can you guess it?", font=("Arial", 12))
result_label.pack(pady=5)

attempts_label = tk.Label(window, text="You have 3 attempts. Good luck!", font=("Arial", 12))
attempts_label.pack(pady=5)

# Pole do wprowadzania liczby
guess_entry = tk.Entry(window, font=("Arial", 12))
guess_entry.pack(pady=5)

# Przycisk do rozpoczecia nowej gry
start_button = tk.Button(window, text="New Game", font=("Arial", 12), command=start_game)
start_button.pack(pady=10)

# Zmienna globalna
max_attempts = 3
attempts = 0

# Rozpoczecie gry
start_game()

# Powiazanie nacisniecia klawisza Enter z funkcja check_guess
guess_entry.bind('<Return>', check_guess)

# Uruchomienie petli Tkinter
window.mainloop()

# Sprawdzenie, czy plik istnieje
if not os.path.exists("game_icon.ico"):
    print("Plik game_icon.ico nie zostal znaleziony w folderze!")
else:
    print("Plik game_icon.ico zostal znaleziony!")
