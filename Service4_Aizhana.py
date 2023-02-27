import time
from sqlQueries import create_table, get_bookings
from credentials import conn
create_table(conn)

if __name__ == '__main__':
    while True:
        bookings = get_bookings(conn)
        print("--------------------Start printing booking data >>")
        for booking in bookings:
            print(booking)
        print("--------------------Ends printing booking data <<")
        time.sleep(5)
