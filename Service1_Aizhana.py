import time
import random
from sqlQueries import create_table, insert_bookings
from bookings import Booking

create_table()

if __name__ == '__main__':
    while True:
        insert_bookings(
            Booking(
                name = random.choice(["Mandarin Oriental Jumeira", "AZUR Regency", "Royal Club","Golden Stay"]),
                type = random.choice(["5 stars", "4 stars", "3 stars","2stars","1 star"]),
                price_for_nights = random.randint(100, 1000),
                rooms = random.randint(1, 100),
                amount = 0,
                numof_travelers = random.randint(1, 10),
                numof_nights = random.randint(1, 30),


            )
        )
        print("Inserted")
        time.sleep(10)
