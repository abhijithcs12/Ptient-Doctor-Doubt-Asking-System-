import mysql.connector

DB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = 'docpy'
)

CR = DB.cursor(dictionary=True)