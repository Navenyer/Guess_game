import os                            # biblioteka systemowa do ikony
import random                        # biblioteka do generowania względnie losowych liczb
import sys                           # biblioteka systemowa do ikony
import tkinter as tk                 # biblioteka  do gui
from tkinter import messagebox       # wywołanie popup info

# zmienna
max_attempts = 3

# globalna zmienna z ilością prób
attempts = 0

# Funkcja do rozpoczęcia nowej gry

def start_game(event=None):                        # Dodajemy event, by obsłużyć zdarzenie New Game
    global secret_number, attempts, max_attempts   # global cdn

    # Aktualny poziom trudności
    difficulty = difficulty_var.get()
    if difficulty == "easy":
        max_attempts = 5
    elif difficulty == "medium":
        max_attempts = 3
    elif difficulty == "hard":
        max_attempts = 1

    # Reset gry
    secret_number = random.randint(1, 10)
    attempts = 0
    result_label.config(
        text=f"Guess a number between 1 and 10! You have {max_attempts} attempts.")
    attempts_label.config(text=f"Attempts left: {max_attempts}")
    guess_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)
    guess_entry.delete(0, tk.END)

# Odblokowanie przyciskow poziomu trudnosci
    easy_button.config(state=tk.NORMAL)
    medium_button.config(state=tk.NORMAL)
    hard_button.config(state=tk.NORMAL)

# Czyszczenie pola wejściowego przy rozpoczęciu nowej gry
    guess_entry.delete(0, tk.END)

def set_difficulty():
    difficulty = difficulty_var.get()
    if difficulty == "easy":
        attempts_label.config(text="Difficulty: Easy - 5 attempts")
    elif difficulty == "medium":
        attempts_label.config(text="Difficulty: Medium - 3 attempts")
    elif difficulty == "hard":
        attempts_label.config(text="Difficulty: Hard - 1 attempt")
     
    start_game()
        
# Funkcja wyłączająca przyciski poziomu trudnosci

def lock_difficulty():
    easy_button.config(state=tk.DISABLED)
    medium_button.config(state=tk.DISABLED)
    hard_button.config(state=tk.DISABLED)

# Funkcja do sprawdzenia zgadywanej liczby
def check_guess(event=None):  # Dodajemy event, by obsłużyć zdarzenie Enter
    global attempts
    if attempts >= max_attempts:
        return  # Uniemożliwienie dalszego zgadywania

    guess = guess_entry.get()

    if is_int_in_range(guess) == True:
        attempts += 1
        guess = int(guess)

        # Blokowanie poziomu trudności po pierwszej próbie
        lock_difficulty()

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
        if attempts >= max_attempts and guess != secret_number:
            result_label.config(
                text=f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}")
            guess_entry.config(state=tk.DISABLED)
            submit_button.config(state=tk.DISABLED)

        # Aktualizacja liczby pozostałych prób
        remaining_attempts = max(0, max_attempts - attempts)
        # attempts_label.config(text=f"Attempts left: {max_attempts - attempts}")
        # Odwołanie do aktualnej wartości max_attempts przy obliczaniu liczby pozostałych prób:
        attempts_label.config(text=f"Attempts left: {remaining_attempts}")

        # Czyszczenie pola wejściowego po naciśnięciu Enter
        guess_entry.delete(0, tk.END)

    else:
        guess_entry.delete(0, tk.END)
        messagebox.showerror(title='Input error',
                             message='Podana liczba musi być liczbą całkowitą w zakresie od 1 do 10')

# CO ta funkcja robi?

def is_int_in_range(number):
    try:
        number = int(number)
        if number >= 0 and number <= 10:
            return True
    except ValueError:
        return False
    except TypeError:
        return False


# Sprawdzamy, czy program jest uruchamiany z pliku .exe NA PROBLEMY Z IKONKA ODTAD
if getattr(sys, 'frozen', False):
    # Jeśli uruchomiono z .exe, ikona będzie w folderze tymczasowym (MEIPASS)
    icon_path = os.path.join(sys._MEIPASS, 'game_icon.ico')
else:
    # Jeśli uruchamiasz w Pythonie, ikona znajduje się w bieżącym katalogu NA PROBLEMY Z IKONKA DOTAD
    icon_path = os.path.join(os.getcwd(), 'game_icon.ico')


# Tworzenie glównego okna
window = tk.Tk()
window.title("Guessing Game")

# Ustawienie ikony gry (plik game_icon.ico musi być w tym samym katalogu)
base_path = getattr(
    sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
icon_path = os.path.join(base_path, "game_icon.ico")
window.iconbitmap(icon_path)

# Ustawienie siatki (grid)
window.rowconfigure([0, 1, 2, 3, 4], weight=1)
window.columnconfigure([0, 1], weight=1)

# Etykiety
welcome_label = tk.Label(
    window, text="Welcome to the guessing game!", font=("Arial", 14))
welcome_label.grid(row=0, column=0, columnspan=2, pady=10)

result_label = tk.Label(
    window, text="I have chosen a number between 1 and 10. Can you guess it?", font=("Arial", 12))
result_label.grid(row=1, column=0, columnspan=2, pady=5)

attempts_label = tk.Label(
    window, text="You have 3 attempts. Good luck!", font=("Arial", 12))
attempts_label.grid(row=4, column=1, columnspan=2, pady=5)

# Pole do wprowadzania liczby
guess_entry = tk.Entry(window, font=("Arial", 12))
guess_entry.grid(row=3, column=1, padx=10, pady=5)

# Przycisk do przesyłania odpowiedzi
submit_button = tk.Button(
    window, text="Press Enter", font=("Arial", 12), command=check_guess)
submit_button.grid(row=3, column=2, padx=10, pady=5)

# Przycisk do rozpoczecia nowej gry
start_button = tk.Button(
    window, text="New Game", font=("Arial", 12), command=start_game)
start_button.grid(row=3, column=0, padx=10, pady=5)

# Przyciski dla wyboru poziomu trudności
difficulty_var = tk.StringVar(value="medium")

easy_button = tk.Radiobutton(window, text="Easy (5 attempts)",
                             variable=difficulty_var, value="easy", command=set_difficulty)
easy_button.grid(row=5, column=0, sticky="w", padx=10)

medium_button = tk.Radiobutton(window, text="Medium (3 attempts)",
                               variable=difficulty_var, value="medium", command=set_difficulty)
medium_button.grid(row=5, column=1, sticky="w", padx=10)

hard_button = tk.Radiobutton(window, text="Hard (1 attempt)",
                             variable=difficulty_var, value="hard", command=set_difficulty)
hard_button.grid(row=5, column=2, sticky="w", padx=10)

# Powiazanie nacisniecia klawisza Enter z funkcja check_guess
guess_entry.bind('<Return>', check_guess)

# Powiązanie naciśnięcia klawisza Spacja z funkcją start_game
# Związanie klawisza Spacja z funkcją
window.bind('<space>', lambda event: start_game())

# Rozpoczecie gry
start_game()

# Uruchomienie pętli Tkinter
window.mainloop()