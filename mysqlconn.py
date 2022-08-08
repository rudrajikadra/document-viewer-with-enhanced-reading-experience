import mysql.connector

# Connect to the mysql database named viewer
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="viewer"
)