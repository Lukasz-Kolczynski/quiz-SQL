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
        {"question": "Jaka jest stolica Francji?", "options": {"a": "Paryż", "b": "Berlin", "c": "Londyn", "d": "Madryt"}, "correct_option": "a"},
        {"question": "Kto napisał 'Romeo i Julia'?", "options": {"a": "William Szekspir", "b": "Charles Dickens", "c": "Jane Austen", "d": "Mark Twain"}, "correct_option": "a"},
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
