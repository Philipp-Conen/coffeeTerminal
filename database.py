import sqlite3
from sqlite3 import Error

def create_connection(path):

    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")

    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def checkCoffee():
    selection = "SELECT coffees FROM users WHERE name = 'Philipp.Conen'"
    c = execute_read_query(connection, selection)
    print(c) 
    return c

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL, 
  gender TEXT,
  coffees INTEGER
);
"""


create_users = """
INSERT INTO
  users (name, gender, coffees)
VALUES
  ('Philipp.Conen','m',0),
  ('Simon.Beckmann','m',0),
  ('Michael.Albrecht','m',0),
  ('Richard.Roedler','m',0),
  ('Florian.Heilemann','m',0),
  ('Johanna.Aigner','f',0);
"""





if __name__ == '__main__':
    connection = create_connection(r"D:\DLR\1_Projekte\coffeeTerminal\cT.db")

#execute_query(connection, create_users_table)
#execute_query(connection, create_users)  

select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

newCoffee = checkCoffee()[0] + 1

update_coffee = """
UPDATE
  users
SET
  coffees = 1
WHERE
  name = 'Philipp.Conen'
"""
execute_query(connection, update_coffee)

checkCoffee()

