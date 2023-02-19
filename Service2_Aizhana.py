import time
from sqlQueries import create_table, set_theamount

create_table()

if __name__ == '__main__':
    while True:
        bookings = set_theamount()
        print("booked")
        time.sleep(5)
