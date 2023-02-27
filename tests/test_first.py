from sqlalchemy import create_engine
from bookings import Booking
from sqlQueries import create_table, insert_bookings, set_theamount, finish, get_bookings


def test_service1(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    booking = Booking(
        name = "test_name",
        type = "5 stars",
        price_for_nights = 1000,
        rooms = 6,
        amount = 3,
        numof_travelers = 6,
        numof_nights = 3,

    )
    insert_bookings(conn, booking)

    bookings = get_bookings(conn)
    assert len(bookings) == 4
    booking = bookings[-1]
    assert booking.name == "test_name"

    set_theamount(conn)
    bookings = get_bookings(conn)
    for booking in bookings:
        assert booking.price_for_nights * booking.numof_nights * booking.numof_travelers == booking.amount
        assert booking.status == "booked"

    finish(conn)
    bookings = get_bookings(conn)
    for booking in bookings:
        assert booking.status == "finished"


