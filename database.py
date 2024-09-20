import sqlite3
connection = sqlite3.connect('ustoz-shogird.db')
cursor = connection.cursor()


def create_db():
    # create condidate table in database 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidate(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        full_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        tools TEXT NOT NULL,
        phone_number VARCHAR(13) NOT NULL,
        location TEXT NOT NULL,
        price TEXT NOT NULL,
        job TEXT NOT NULL,
        time TEXT NOT NULL,
        aim TEXT NOT NULL
    )
    """)


    connection.commit()

create_db()


def insert_data_db(full_name, type, age, tools, phone_number, location, price, job, time, aim):
    cursor.execute('INSERT INTO candidate (full_name, type, age, tools, phone_number, location, price, job, time, aim) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (full_name, type, age, tools, phone_number, location, price, job, time, aim))
    connection.commit()


def get_candidates():
    return cursor.execute('SELECT * FROM candidate').fetchall()

def delete():
    return cursor.execute('DELETE FROM candidate WHERE id = ?', ('1',)).fetchall()
connection.commit()


def update_candidate(id, age):
    cursor.execute('UPDATE candidate SET age = ? WHERE id = ?', (age, id,))
    connection.commit


def select_candidate(id):
    return cursor.execute('SELECT * FROM candidate WHERE id = ?', (id,)).fetchone()
connection.commit

# insert_data_db('Usmon', 'Ish kerak', 15, 'Python, Django', '+998946675649', 'Toshkent', 'Tekin', 'Ish kerak', 'Kechasi', 'Programist')

def delete_candidate(id):
    return cursor.execute('DELETE FROM candidate WHERE id = ?', (id,)).fetchone()
connection.commit

# print(get_candidates())

# print(delete())

# delete_candidate(3)
# print(select_candidate(3))

# update_candidate(2, 19)
# print(get_candidates())


connection.close()























