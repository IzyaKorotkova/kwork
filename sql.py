import mysql.connector
from mysql.connector import Error
from mysql.connector.locales.eng import client_error

def create_connection_db(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection_db("31.28.27.213", "root", "луу1947*", "airplane")

def add_flight_schedule(date, time, fromPlace, toPlace,  flight_id, place_free):
    cursor = connection.cursor()
    Y, M, D = date.split('.')
    date = f"{D}.{M}.{Y}"
    cursor.execute("INSERT INTO airplane (date_fly, time_fly, from_place, to_place,flight_id,free_place) VALUES (%s,%s,%s,%s,%s,%s)", (date, time,  toPlace, fromPlace, flight_id, place_free))
    connection.commit()
    cursor.close()

def change_flight_schedule(id, date, time, fromPlace, toPlace,  flight_id, place_free):
    cursor = connection.cursor()
    Y, M, D = date.split('.')
    date = f"{D}.{M}.{Y}"
    cursor.execute("UPDATE airplane SET date_fly = %s, time_fly = %s, from_place = %s, to_place = %s, flight_id = %s, free_place = %s WHERE id = %s", (date, time,  toPlace, fromPlace, flight_id, place_free, id))
    connection.commit()
    cursor.close()

def get_city(city):
    cursor = connection.cursor()
    insert_movies_query = "Select city.city from city where city.city= '" + city + "'"
    cursor.execute(insert_movies_query)
    city_schedule = cursor.fetchall()
    cursor.close()
    if len(city_schedule) == 0:
        return ''
    return city_schedule[0][0]

def get_city_2(city):
    cursor = connection.cursor()
    insert_movies_query = "Select city.id from city where city.city= '" + city + "'"
    cursor.execute(insert_movies_query)
    city_schedule = cursor.fetchall()
    cursor.close()
    if len(city_schedule) == 0:
        return ''
    return city_schedule[0][0]

def add_city(city):
    cursor = connection.cursor()
    city_2 = get_city(city)
    if city_2 != city:
        insert_movies_query = "INSERT INTO city (city) VALUES ('" + city + "')"
        cursor.execute(insert_movies_query)
        connection.commit()
    cursor.close()

def delete_city(city):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM city WHERE city=%s", (city,))
    connection.commit()
    cursor.close()

def change_city(city_1, city_2):
    cursor = connection.cursor()
    if get_city_2(city_2) == '':
        cursor.execute("UPDATE city SET city = %s WHERE city = %s", (city_2, city_1))
    connection.commit()
    cursor.close()

def get_flight(flight):
    cursor = connection.cursor()
    insert_movies_query = "Select flight.flight from flight where flight.flight= '" + flight + "'"
    cursor.execute(insert_movies_query)
    flight_schedule = cursor.fetchall()
    cursor.close()
    if len(flight_schedule) == 0:
        return ''
    return flight_schedule[0][0]

def get_flight_2(flight):
    cursor = connection.cursor()
    insert_movies_query = "Select flight.id from flight where flight.flight= '" + flight + "'"
    cursor.execute(insert_movies_query)
    flight_schedule = cursor.fetchall()
    cursor.close()
    if len(flight_schedule) == 0:
        return ''
    return flight_schedule[0][0]

def add_flight(flight):
    cursor = connection.cursor()
    flight_2 = get_flight(flight)
    if flight_2 != flight:
        query = "INSERT INTO flight (flight) VALUES ('" + flight + "')"
        cursor.execute(query)
        connection.commit()
    cursor.close()

def delete_flight(flight):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM flight WHERE flight=%s", (flight,))
    connection.commit()
    cursor.close()

def change_flight(flight_1, flight_2):
    cursor = connection.cursor()
    cursor.execute("UPDATE flight SET flight = %s WHERE flight = %s", (flight_2, flight_1))
    connection.commit()
    cursor.close()

def delete_airplane(id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM airplane WHERE id=%s", (id,))
    connection.commit()
    cursor.close()


def edit_flight_schedule(date_fly, time_fly, from_place, to_place, flight_id, free_place):
    cursor = connection.cursor()
    query = "UPDATE airplane SET date_fly= %s, time_fly = %s, from_place = %s, to_place = %s, flight_id = %s free_place = %s WHERE id = %s"
    cursor.execute(query, (date_fly, time_fly, from_place, to_place, flight_id, free_place))
    connection.commit()
    cursor.close()

def get_airplane():
    cursor = connection.cursor()
    select_flight_query = "Select a.id, DATE_FORMAT(a.date_fly, '%d-%m-%Y'), a.time_fly, c.city as from_place, s.city as to_place, f.flight as flight_id , a.free_place FROM airplane as a join flight as f on a.flight_id = f.Id join city as s on a.to_place = s.Id join city as c on a.from_place = c.Id"
    cursor.execute(select_flight_query)
    flight_schedule = cursor.fetchall()
    cursor.close()
    return flight_schedule

def get_flight_where(where):
    cursor = connection.cursor()
    select_flight_query = "Select a.id, DATE_FORMAT(a.date_fly, '%d-%m-%Y'), a.time_fly, c.city as from_place, s.city as to_place, f.flight as flight_id , a.free_place FROM airplane as a join flight as f on a.flight_id = f.Id join city as s on a.to_place = s.Id join city as c on a.from_place = c.Id where " + where
    cursor.execute(select_flight_query)
    flight_schedule = cursor.fetchall()
    cursor.close()
    return flight_schedule

def get_airplane_2(checked_options):
    cursor = connection.cursor()
    join = ""
    select_flight_query = "Select "

    if 'Дата' in checked_options:
        select_flight_query += "DATE_FORMAT(a.date_fly, '%d-%m-%Y'),"
    if 'Время' in checked_options:
        select_flight_query += "a.time_fly,"
    if 'Пункт отправления' in checked_options:
        select_flight_query += "c.city as from_place,"
        join += "join city as c on a.from_place = c.Id "
    if 'Пункт прибытия' in checked_options:
        select_flight_query += "s.city as to_place,"
        join += "join city as s on a.to_place = s.Id "
    if 'Рейс' in checked_options:
        select_flight_query += "f.flight as flight_id,"
        join += "join flight as f on a.flight_id = f.Id "
    if 'Места' in checked_options:
        select_flight_query += "a.free_place,"
    select_flight_query = select_flight_query[:-1]
    select_flight_query += " FROM airplane as a " + join
    cursor.execute(select_flight_query)
    flight_schedule = cursor.fetchall()
    cursor.close()
    return flight_schedule
