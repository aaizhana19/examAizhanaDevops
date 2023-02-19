import psycopg2

from bookings import Booking

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)


def create_table():
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
        check_in  DATE DEFAULT '2023,2,10',
        check_out DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'free'
        
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_bookings(bookings: Booking):
    query = """
    INSERT INTO bookings (name, type, price_for_nights, rooms, amount, numof_travelers, numof_nights)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (bookings.name, bookings.type, bookings.price_for_nights, bookings.rooms, bookings.amount,
                           bookings.numof_travelers,bookings.numof_nights ))
    conn.commit()


def set_theamount():
    query = "UPDATE bookings SET amount=price_for_nights * numof_nights * numof_travelers, status='booked' WHERE status='free';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def finish():
    query = "UPDATE bookings SET status='finished' WHERE status='booked';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def get_bookings() -> list[Booking]:
    query = "SELECT * FROM bookings;"
    cursor = conn.cursor()
    cursor.execute(query)
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



    ) for bookings in cursor.fetchall()]
