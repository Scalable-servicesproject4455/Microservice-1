import mysql.connector

def get_all_temperatures():
    conn = mysql.connector.connect(host='mysql-db', port=3306, user='root', password='root', database='temp_db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM temp_service")
    rows = cursor.fetchall()
    conn.close()
    return [dict(room_id=row[0], temperature=row[1]) for row in rows]

def get_temperature_by_room_id(room_id):
    conn = mysql.connector.connect(host='mysql-db', port=3306, user='root', password='root', database='temp_db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM temp_service WHERE room_id = %s", (room_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(room_id=row[0], temperature=row[1]) if row else {}
