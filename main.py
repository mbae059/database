import getpass

import psycopg2
import user
if __name__ == '__main__':
    user = user.User()

    con = psycopg2.connect(
        database = 'sample2023',
        user = 'db2023',
        password = 'db!2023',
        host = '::1',
        port = '5432',
    )

    cursor = con.cursor()
    user.login(cursor)