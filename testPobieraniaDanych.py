import mysql.connector

# Funkcja tworząca połączenie z bazą danych
def connect_to_quiz():
    try:
        connection = mysql.connector.connect(
            host="***********",
            user="*********",
            password="********",
            database="********" 
        )
        return connection
    except mysql.connector.Error as err:
        print("Błąd połączenia z bazą danych:", err)

# Funkcja pobierająca dane z bazy danych
def get_data_from_quiz(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(cursor.execute("SELECT * FROM user") # Zapytanie SQL do pobrania danych
        rows = cursor.fetchall() 
        column_names = [i[0] for i in cursor.description]  
        cursor.close()
        return column_names, rows
    except mysql.connector.Error as err:
        print("Błąd podczas pobierania danych z bazy danych:", err)

# Połączenie z bazą danych
connection = connect_to_quiz()

if connection:
    column_names, data = get_data_from_quiz(connection)
    if data:
        for row in data:
            for column_name, value in zip(column_names, row):
                print(f"{column_name}: {value}") 
            print()  
    connection.close()
