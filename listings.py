import logging
import time

def create_listing(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS listing (id INT PRIMARY KEY, name STRING, address STRING, rent INT, bedroom INT)"
        )
        cur.execute("UPSERT INTO listing (id, name, address, rent, bedroom) VALUES (1, 'small bedroom', '23 Vermont LA CA 90007', 950, 1), (2, 'studio', '532 Normandie LA CA 90007', 800, 1), (3, 'big bedroom', '234 Vermont LA CA 90007', 1200, 1), (4, 'sweet housing', '1123 Normandie LA CA 90007', 4300, 3)")
        logging.debug("create_listing(): status message: %s", cur.statusmessage)
    conn.commit()


def delete_listing(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM listing")
        logging.debug("delete_listing(): status message: %s", cur.statusmessage)
    conn.commit()


def print_listing(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, address FROM listing")
        logging.debug("print_listing(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        print(f"listing at {time.asctime()}:")
        for row in rows:
            print(row)
            
    return rows