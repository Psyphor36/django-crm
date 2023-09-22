import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

#preparing a cursor
cursorobj = db.cursor()

#creating a db
cursorobj.execute("CREATE DATABASE websitedb")

print('Done!')
