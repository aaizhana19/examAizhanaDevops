import time
from sqlQueries import create_table, finish
from credentials import conn
create_table(conn)

if __name__ == '__main__':
    while True:
        bookings = finish(conn)
        print("finished")
        time.sleep(5)

