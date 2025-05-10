import mysql.connector

def insert_temperature(temperature):
    conn = mysql.connector.connect(host='mysql-db', port=3306, user='root', password='root', database='temp_db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO temp_service (temperature) VALUES (%s)", (temperature,))
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id

def insert_multiple_temperatures(temp_list):
    conn = mysql.connector.connect(host='mysql-db', port=3306, user='root', password='root', database='temp_db')
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO temp_service (temperature) VALUES (%s)", [(t,) for t in temp_list])
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount
