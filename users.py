import logging
import time

def create_user(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, firstname STRING, lastname STRING, email STRING, phone INT, passward STRING)"
        )
        cur.execute("UPSERT INTO users (id, firstname, lastname, email, phone, passward) VALUES (1, 'Sonia', 'Zhang', 'wenyue@usc.edu', 2321311322, '123456'), (2, 'Jenny', 'Doni', 'jenny@usc.edu', 3647378238, '123456'), (3, 'Yanny', 'Hia', 'yanny@usc.edu', 3641918238, '123456')")
        logging.debug("create_user(): status message: %s", cur.statusmessage)
    conn.commit()


def delete_user(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM users")
        logging.debug("delete_user(): status message: %s", cur.statusmessage)
    conn.commit()


def print_user(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id, firstname, lastname FROM users")
        logging.debug("print_user(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        print(f"user at {time.asctime()}:")
        for row in rows:
            print(row)
    return rows