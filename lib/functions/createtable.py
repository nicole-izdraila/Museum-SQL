# imports 
import mysql.connector
from mysql.connector import errorcode


# create table function
def createTableDef(cnx, cursor):
    print('\n--------------- SQL command CREATE TABLE -----------------\n')
    
    # example of the sql command
    print('To use the CREATE TABLE SQL Command follow the example below.\n')
    print('***************** EXAMPLE *******************\n')
    print('CREATE TABLE PERSONS(\nPersonID INT PRIMARY KEY,\nLName VARCHAR(25) NOT NULL,\nFName VARCHAR(25) NOT NULL,\nADDRESS VARCHAR(20),\nCITY VARCHAR(30) FOREIGN KEY REFERENCES TICKET_DESTINATION(CITY));')
    print('\n*********************************************\n')

    # table name
    tableName = input('Insert the name of the new table: ')
    
    # attributes sentence
    attributes = input('Insert the attributes of the new table.\n(Use comma after every statement. Be precise as possible with the names, datatypes and constraints following the example above.): ')
    
    print('\n--------------------------------------------------------------------\n')
    
    # tables tuple
    TABLES = {}
    
    TABLES[tableName.upper()] = ('CREATE TABLE IF NOT EXISTS {} ({}) ENGINE=InnoDB'.format(tableName.upper(), attributes))
    for table_name in TABLES:
        sqlCommand = TABLES[table_name]
        try:
            cursor.execute(sqlCommand)
            print('SQL command executed: ', sqlCommand)
            print('Creating table ({})\n'.format(table_name.upper()))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))