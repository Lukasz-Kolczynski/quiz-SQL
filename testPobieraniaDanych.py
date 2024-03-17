import mysql.connector

# Funkcja tworząca połączenie z bazą danych
def connect_to_quiz():
    try:
        connection = mysql.connector.connect(
            host="****************",
            user="****************",
            password="**********",
            database="****************"  # Nazwa Twojej bazy danych
        )
        return connection
    except mysql.connector.Error as err:
        print("Błąd połączenia z bazą danych:", err)

# Funkcja pobierająca dane z bazy danych
def get_data_from_quiz(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT user_name,user_score FROM user order by user_score DESC LIMIT 3")  # Zapytanie SQL do pobrania danych
        
        rows = cursor.fetchall()  # Pobranie wszystkich wierszy
        column_names = [i[0] for i in cursor.description]  # Pobranie nazw kolumn
        cursor.close()
        return column_names, rows
    except mysql.connector.Error as err:
        print("Błąd podczas pobierania danych z bazy danych:", err)

# Połączenie z bazą danych
connection = connect_to_quiz()

# Pobranie danych z bazy danych
if connection:
    column_names, data = get_data_from_quiz(connection)
    if data:
        print("TOP 3 miejsca:")
        miejsce = 1 
        for miejsce, row in enumerate(data[:3], 1):
            print(f"Miejsce {miejsce} należy do: ")
            for column_name, value in zip(column_names, row):
                print(f"{column_name}: {value}")
            print() 
    connection.close()
