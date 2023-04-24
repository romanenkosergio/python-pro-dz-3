import sqlite3
from faker import Faker

fake = Faker()


def init_db():
    """Initialize the database"""
    connection = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    # Insert fake data
    for _ in range(200):
        cur.execute("INSERT INTO customers (first_name, last_name, age) VALUES (?, ?, ?)",
                    (fake.first_name(), fake.last_name(), fake.date_of_birth())
                    )
        cur.execute("INSERT INTO tracks (track_name, duration) VALUES (?, ?)",
                    (fake.text(max_nb_chars=20), fake.time(pattern="%S"))
                    )
    connection.commit()
    connection.close()


def get_db_connection():
    # Create a connection to the database
    con = sqlite3.connect('database.db')
    return con