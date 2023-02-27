import psycopg2
from sqlalchemy.engine import Connection
from sqlalchemy import text

from bookings import Booking



def create_table(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS bookings (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        type VARCHAR(255) NOT NULL,
        price_for_nights INTEGER NOT NULL,
        rooms INTEGER,
        amount INTEGER,
        numof_travelers INTEGER NOT NULL,
        numof_nights INTEGER NOT NULL,
        check_in  DATE DEFAULT ((current_date - INTERVAL '2 day')::date),
        check_out DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'free'
        
        )
    """


    conn.execute(text(query))
    conn.commit()


def insert_bookings(conn: Connection, bookings: Booking):
    query = """
    INSERT INTO bookings (name, type, price_for_nights, rooms, amount, numof_travelers, numof_nights)
    VALUES (:name, :type, :price_for_nights, :rooms,:amount,:numof_travelers,:numof_nights)
    """


    conn.execute(text(query),
                 parameters = {
                     "name" : bookings.name,
                     "type" : bookings.type,
                     "price_for_nights" : bookings.price_for_nights,
                     "rooms": bookings.rooms,
                     "amount": bookings.amount,
                     "numof_travelers" : bookings.numof_travelers,
                     "numof_nights" : bookings.numof_nights,
                 },
                 )
    conn.commit()


def set_theamount(conn: Connection):
    query = "UPDATE bookings SET amount=price_for_nights * numof_nights * numof_travelers, status='booked' WHERE status='free';"
    conn.execute(text(query))
    conn.commit()


def finish(conn: Connection):
    query = "UPDATE bookings SET status='finished' WHERE status='booked';"
    conn.execute(text(query))
    conn.commit()

def get_bookings(conn: Connection) -> list[Booking]:
    query = "SELECT * FROM bookings;"
    bookingss = conn.execute(text(query)).fetchall()
    return [Booking(
        id =  bookings[0],
        name = bookings[1],
        type =  bookings[2],
        price_for_nights = bookings[3],
        rooms = bookings[4],
        amount = bookings[5],
        numof_travelers = bookings[6],
        numof_nights = bookings[7],
        check_in = bookings[8],
        check_out = bookings[9],
        status = bookings[10],



    ) for bookings in bookingss]
