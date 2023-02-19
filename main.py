import psycopg2

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)

if __name__ == '__main__':
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS bookings")
    print("deleted")

