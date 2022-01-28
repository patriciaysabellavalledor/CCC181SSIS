from dotenv import load_dotenv
import mysql.connector as mysql
from os import getenv
load_dotenv ()


db = mysql.connect(
    host = getenv('DB_HOST'),
    user = getenv('DB_USER'),
    password = getenv('DB_PASSWORD'),
    database = getenv('DB_NAME')
)

cursor = db.cursor()
