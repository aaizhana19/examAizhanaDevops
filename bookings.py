from dataclasses import dataclass, field
from datetime import datetime

from psycopg2._psycopg import DATE
from typing import Optional


@dataclass
class Booking:
    name: str
    type: str
    price_for_nights: int
    rooms: int
    amount: int
    numof_travelers: int
    numof_nights: int
    check_in: str =''
    check_out: str = ''
    status: str = "free"
    id: Optional[int] = None



