import sqlalchemy
from typing import Generator
import pytest
from sqlalchemy import Connection, create_engine
from testcontainers.postgres import PostgresContainer

from sqlQueries import create_table, insert_bookings
from bookings import Booking


@pytest.fixture()
def postgres_container1() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer(image="postgres:latest") as container:
        container.get_container_host_ip = lambda: 'localhost'
        container.start()
        yield container


@pytest.fixture()
def postgres_container() -> PostgresContainer:
    container = PostgresContainer(image="postgres:latest")
    container.get_container_host_ip = lambda: 'localhost'
    container.start()
    return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    return postgres_container.get_connection_url()


@pytest.fixture(scope="function")
def conn_with_data(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    bookings = [
        Booking(
            name = "test_name 1",
            type = "3 stars",
            price_for_nights = 5000,
            rooms = 10,
            amount = 450,
            numof_travelers = 2,
            numof_nights = 5,
        ),
        Booking(
            name = "test_name 2",
            type = "2 stars",
            price_for_nights = 600,
            rooms = 1,
            amount = 100,
            numof_travelers = 1,
            numof_nights = 2,
        ),
        Booking(
            name = "test_name 3",
            type = "5 stars",
            price_for_nights = 1200,
            rooms = 4,
            amount = 1500,
            numof_travelers = 4,
            numof_nights = 2,
        ),
    ]
    for booking in bookings:
        insert_bookings(conn, booking)
    return postgres_container.get_connection_url()
