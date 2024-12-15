import os
import random
import sys
import tkinter as tk
from tkinter import messagebox

# stała
MAX_ATTEMPTS = 3

# globalna zmienna z ilością prób
attempts = 0

# Funkcja do rozpoczęcia nowej gry

def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 10)
    attempts = 0
    result_label.config(
        text=f"Guess a number between 1 and 10! You have {MAX_ATTEMPTS} attempts.")
    guess_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)

# Czyszczenie pola wejściowego przy rozpoczęciu nowej gry
    guess_entry.delete(0, tk.END)


# Funkcja do sprawdzenia zgadywanej liczby
def check_guess(event=None):  # Dodajemy event, by obsłużyć zdarzenie Enter
    global attempts
    guess = guess_entry.get()

    if is_int_in_range(guess) == True:
        attempts += 1
        guess = int(guess)

        if guess < secret_number:
            result_label.config(text="Too low! Try again.")
        elif guess > secret_number:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(
                text=f"Congratulations! You guessed it in {attempts} attempts!")
            guess_entry.config(state=tk.DISABLED)
            submit_button.config(state=tk.DISABLED)

        # Sprawdzenie, czy gracz przekroczył liczbę prób
        if attempts >= MAX_ATTEMPTS and guess != secret_number:
            result_label.config(
                text=f"Sorry, you've used all {MAX_ATTEMPTS} attempts. The number was {secret_number}")
            guess_entry.config(state=tk.DISABLED)
            submit_button.config(state=tk.DISABLED)

        # Czyszczenie pola wejściowego po naciśnięciu Enter
        guess_entry.delete(0, tk.END)

    else:
        guess_entry.delete(0, tk.END)
        messagebox.showerror(title='Input error',
                             message='Podana liczba musi być liczbą całkowitą w zakresie od 1 do 10')



def is_int_in_range(number):
    try:
        number = int(number)
        if number >= 0 and number <= 10:
            return True
    except ValueError:
        return False
    except TypeError:
        return False


# Tworzenie głównego okna
window = tk.Tk()
window.title("Guessing Game")

# Ustawienie ikony gry (plik game_icon.ico musi być w tym samym katalogu)

base_path = getattr(sys, '_MEIPASS', os.path.dirname(
     os.path.abspath(__file__)))
icon_path = os.path.join(base_path, "game_icon.ico")
window.iconbitmap(icon_path)

# Etykiety
welcome_label = tk.Label(
    window, text="Welcome to the guessing game!", font=("Arial", 14))
welcome_label.pack(pady=10)

result_label = tk.Label(
    window, text="I have chosen a number between 1 and 10. Can you guess it?", font=("Arial", 12))
result_label.pack(pady=5)

attempts_label = tk.Label(
    window, text="You have 3 attempts. Good luck!", font=("Arial", 12))
attempts_label.pack(pady=5)

# Pole do wprowadzania liczby
guess_entry = tk.Entry(window, font=("Arial", 12))
guess_entry.pack(pady=5)

# Przycisk do przesyłania odpowiedzi
submit_button = tk.Button(window, text="Press Enter",
                          font=("Arial", 12), command=check_guess)
submit_button.pack(pady=5)

# Przycisk do rozpoczęcia nowej gry
start_button = tk.Button(window, text="Spacebar = New Game",
                         font=("Arial", 12), command=start_game)
start_button.pack(pady=10)

# Powiązanie naciśnięcia klawisza Spacja z funkcją start_game
start_button.bind('<space>', start_game)  # Związanie klawisza Spacja z funkcją

# Rozpoczęcie gry
start_game()

# Powiązanie naciśnięcia klawisza Enter z funkcją check_guess
guess_entry.bind('<Return>', check_guess)  # Związanie Enter z funkcją

# Uruchomienie pętli Tkinter
window.mainloop()

# diagnostyka ikony

# Sprawdzenie, czy plik istnieje
if not os.path.exists("game_icon.ico"):
    print("Plik game_icon.ico nie został znaleziony w folderze!")
else:
    print("Plik game_icon.ico został znaleziony!")
