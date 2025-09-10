# Write a simple python script that creates the database alx_book_store 
# in your MySQL server.

# Name of python script should be MySQLServer.py
# If the database alx_book_store already exists, your script should not fail
# You are not allowed to use the 
# NOTE :

# Required to print message such as Database 'alx_book_store' created successfully! 
# when database is successfully created.

# Print error message to handle errors when failing to connect to the DB.

# handle open and close of the DB in your script.

# Repo:

# GitHub repository: Intro_to_DB
# File: MySQLServer.py

import mysql.connector

db = mysql.connector.connect(
    hostname ="localhost",
    username = "alx",
    password = "alx"
)

cursor =  db.cursor()

sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"

try :
    cursor.execute(sql)
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print(f'Error: {err}')