import time
from sqlQueries import create_table, get_bookings

create_table()

if __name__ == '__main__':
    while True:
        bookings = get_bookings()
        print("--------------------Start printing booking data >>")
        for booking in bookings:
            print(booking)
        print("--------------------Ends printing booking data <<")
        time.sleep(5)
