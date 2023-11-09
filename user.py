import getpass
import psycopg2
class User:
    def __init__(self):
        self.name = ""

    def login(self, cursor):
        id = input("ID: ")
        password = getpass.getpass("password: ")

        print(id, password)

        print(f'select balance from customers where customer_id={id}')
        cursor.execute(f'select balance from customers where customer_id={id}')

        result = cursor.fetchall()
        print(result[0])
        # if id and password matches then pass
        # if it doesn't then return false