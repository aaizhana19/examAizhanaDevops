import time
from sqlQueries import create_table, finish

create_table()

if __name__ == '__main__':
    while True:
        bookings = finish()
        print("finished")
        time.sleep(5)

