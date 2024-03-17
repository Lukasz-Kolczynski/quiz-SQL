import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Funkcja tworząca połączenie z bazą danych
def connect_to_*******():
    try:
        connection = mysql.connector.connect(
            host="***************",
            user="*********",
            password="***********",
            database="**********"  # Nazwa Twojej bazy danych
        )
        return connection
    except mysql.connector.Error as err:
        print("Błąd połączenia z bazą danych:", err)

# Funkcja tworząca nowego użytkownika
def create_user(connection, username):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user (user_name) VALUES (%s)", (username,))
        connection.commit()
        cursor.close()
        print("Użytkownik", username, "został utworzony.")
    except mysql.connector.Error as err:
        print("Błąd podczas tworzenia użytkownika:", err)

# Funkcja przeprowadzająca quiz
def run_quiz(connection, username):
    score = 0
    questions = [
        {"question": "Jaki jest skrót od Structured Query Language?", "options": {"a": "SQR", "b": "SQL", "c": "SQRL", "d": "STQL"}, "correct_option": "b"},
        {"question": "W jaki sposób wybieramy wszystkie kolumny z tabeli w zapytaniu SQL?", "options": {"a": "SELECT *", "b": "SELECT ALL", "c": "SELECT COLUMN", "d": "SELECT FIELDS"}, "correct_option": "a"},
        {"question": "Który z poniższych operatorów jest używany do sprawdzania przynależności elementu do listy w Pythonie?", "options": {"a": "::", "b": "<>", "c": "in", "d": "><"}, "correct_option": "c"},
        {"question": "Jakie są typowe rodzaje wyjątków w Pythonie?", "options": {"a": "Normal i Critical", "b": "Primary i Secondary", "c": "Syntax i Logic", "d": "Standard i Custom"}, "correct_option": "c"},
        {"question": "Jaki operator jest używany do alokacji pamięci w C++?", "options": {"a": "alloc", "b": "allocate", "c": "malloc", "d": "new"}, "correct_option": "d"},
        {"question": "Które z poniższych jest wierszem komentarza w języku C?", "options": {"a": "//", "b": "--", "c": "''", "d": "##"}, "correct_option": "a"},
        {"question": "Które polecenie SQL służy do dodawania nowych rekordów do tabeli?", "options": {"a": " INSERT INTO", "b": "ADD RECORD", "c": "UPDATE", "d": "CREATE"}, "correct_option": "a"},
        {"question": "Który operator logiczny w Pythonie zwraca True, jeśli przynajmniej jeden warunek jest spełniony?", "options": {"a": "||", "b": "&&", "c": "or", "d": "and"}, "correct_option": "c"},

        # Dodaj więcej pytań według potrzeb
    ]

    def check_answer():
        nonlocal score
        nonlocal current_question_index
        selected_option = selected_option_var.get()
        if selected_option == questions[current_question_index]["correct_option"]:
            score += 1
        current_question_index += 1
        next_question()

    def next_question():
        nonlocal current_question_index
        if current_question_index < len(questions):
            question_label.config(text=questions[current_question_index]["question"])
            for option, answer in questions[current_question_index]["options"].items():
                option_buttons[option].config(text=answer)
            selected_option_var.set("")
        else:
            messagebox.showinfo("Quiz zakończony", f"Twój wynik: {score}/{len(questions)}")
            update_score(connection, username, score)
            window.quit()

    def set_selected_option(option):
        selected_option_var.set(option)
        check_answer()

    window = tk.Tk()
    window.title("Quiz")
    window.geometry("400x300")

    question_label = tk.Label(window, text="", wraplength=380, justify="center")
    question_label.pack(pady=10)

    option_buttons = {}
    selected_option_var = tk.StringVar()

    current_question_index = 0

    for option in ["a", "b", "c", "d"]:
        option_buttons[option] = tk.Button(window, text="", command=lambda option=option: set_selected_option(option))
        option_buttons[option].pack(pady=5)

    next_question()

    window.mainloop()

# Funkcja aktualizująca wynik użytkownika w bazie danych
def update_score(connection, username, score):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE user SET user_score = %s WHERE user_name = %s", (score, username))
        connection.commit()
        cursor.close()
        print("Wynik użytkownika", username, "został zaktualizowany.")
    except mysql.connector.Error as err:
        print("Błąd podczas aktualizacji wyniku użytkownika:", err)

def main():
    connection = connect_to_*********()
    if connection:
        username = input("Podaj swoją nazwę użytkownika: ")
        create_user(connection, username)
        run_quiz(connection, username)
        connection.close()

if __name__ == "__main__":
    main()
