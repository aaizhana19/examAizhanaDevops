import time
from sqlQueries import create_table, set_theamount
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        bookings = set_theamount(conn)
        print("booked")
        time.sleep(5)
