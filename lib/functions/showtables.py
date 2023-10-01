# imports 
import mysql.connector
from mysql.connector import errorcode


# show tables function
def showTablesDef(cnx, cursor):
    try:
        sqlCommand = ('SHOW TABLES;')
        cursor.execute(sqlCommand)
        print('\n--------------- Tables in Database -----------------\n')
        for table in cursor:
            print(table[0])
        print('\n---------------------------------------------------\n')
    except mysql.connector.Error as err:
            print('Error: {}'.format(err))