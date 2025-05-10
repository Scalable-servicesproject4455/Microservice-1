import mysql.connector

def update_temperature_by_room_id(room_id, new_temp):
    conn = mysql.connector.connect(host='mysql-db', port=3306, user='root', password='root', database='temp_db')
    cursor = conn.cursor()
    cursor.execute("UPDATE temp_service SET temperature = %s WHERE room_id = %s", (new_temp, room_id))
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount
