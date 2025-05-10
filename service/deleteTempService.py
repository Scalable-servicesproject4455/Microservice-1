import mysql.connector
from mysql.connector import Error
import logging



# --- temp_service_deletes.py ---
def delete_by_room_id(room_id):
    conn = mysql.connector.connect(host='mysql-db', port=3306, user='root', password='root', database='temp_db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM temp_service WHERE room_id = %s", (room_id,))
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount

def delete_all_temperatures():
    conn = mysql.connector.connect(host='mysql-db', port=3306, user='root', password='root', database='temp_db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM temp_service")
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    return rowcount
