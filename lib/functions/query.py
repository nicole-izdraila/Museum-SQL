import mysql.connector
from mysql.connector import errorcode
from functions.showtables import showTablesDef

# query function
def queryDef(cnx, cursor):
    
    print('\n--------------- Select to use a SQL Query command -----------------\n')
    
    # example of the sql command
    print('To use a SQL Query Command follow the example below.\n')
    print('***************** EXAMPLE *******************\n')
    print("SELECT PersonID, FName, LName\nFROM PERSONS\nWHERE BirthYear = 2002 AND Sex = 'M';")
    print()
    print("SELECT *\nFROM PERSONS")
    print('\n*******************************************\n')
    
    # query commands
    print('1. With WHERE condition')
    print('2. Without WHERE condition')
    
    print('\n--------------------------------------------------------------------\n')

    # table selection
    querySelection = input('Select a number: ')
    
    # query w/ WHERE condition
    if querySelection == '1':
        
        # show tables
        showTablesDef(cnx, cursor)
        
        # select statement
        select = input('Insert condition SELECT (Condition Select accepts multiple arguments separated by a comma. Be precise as possible with the column names following the example above): ')
        
        # table name
        table = input('Insert the name of the table (Be precise as possible following the example above): ')
        
        # where statement
        where = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        
        try:
            sqlCommand = ("SELECT {} FROM {} WHERE {};".format(select, table.upper(), where))
            cursor.execute(sqlCommand)
            query = cursor.fetchall()
            print('\nSuccessfully running query command!\n')
            for row in range(len(query)):
                for column in range(len(query[row])):
                    print(query[row][column], end=' ')
                print()
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # query w/o WHERE condition
    elif querySelection == '2':
        
        # show tables
        showTablesDef(cnx, cursor)
        
        # select statement
        select = input('Insert condition SELECT (Condition Select accepts multiple arguments separated by a comma. Be precise as possible with the column names following the example above): ')
        
        # table name
        table = input('Insert the name of the table (Be precise as possible following the example above): ')
        
        try:
            sqlCommand = ("SELECT {} FROM {};".format(select, table.upper()))
            cursor.execute(sqlCommand)
            query = cursor.fetchall()
            print('\nSuccessfully running query command!\n')
            for row in range(len(query)):
                for column in range(len(query[row])):
                    print(query[row][column], end=' ')
                print()
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))