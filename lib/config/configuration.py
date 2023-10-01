# imports
import mysql.connector
from mysql.connector import errorcode


# MySQL class
class MySql:
    
    # private members
    __user = None
    __password = None
    __host = None
    __database = None
    
    # constructor
    def __init__(self, password):
        self.__user = 'root'
        self.__password = password
        self.__host = 'localhost'
        self.__database = 'ART_OBJECT'
    
    # user creator
    def myUser(self):
        config = {
            'user': self.__user,
            'password': self.__password,
            'host': self.__host,
            'database': self.__database
        }
        return config
    
    # connection to database
    def myConnection(self):    
        try:
            cnx = mysql.connector.connect(**self.myUser())
            print("Successfully connected to the database!")
            return cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: Something is wrong with your user name or password.\n")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Error: Database does not exist.\n")
            else:
                print(err)