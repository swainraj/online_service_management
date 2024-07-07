import mysql.connector
from config import Config

db = mysql.connector.connect(
    host=Config.MYSQL_HOST,
    user=Config.MYSQL_USER,
    passwd=Config.MYSQL_PASSWORD,
    database=Config.MYSQL_DB
)

cursor = db.cursor()
cursor.execute("UPDATE cases SET status='closed' WHERE status!='closed' AND DATE_ADD(created_at, INTERVAL 7 DAY) < NOW()")
db.commit()
db.close()
