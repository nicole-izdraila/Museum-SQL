# imports
import mysql.connector
from mysql.connector import errorcode
from functions.showtables import showTablesDef


# alter function
def alterDef(cnx, cursor):
    print('\n--------------- Select to use SQL command ALTER TABLE-----------------\n')
    
    # example of the sql command
    print('To use the ALTER TABLE SQL Command follow the example below.\n')
    print('***************** EXAMPLE *******************\n')
    print("ALTER TABLE PERSONS\nADD Email VARCHAR(25);")
    print()
    print("ALTER TABLE PERSONS\nDROP COLUMN Email;")
    print()
    print("ALTER TABLE PERSONS\nMODIFY COLUMN BirthYear year;")
    print('\n*******************************************\n')
    
    # alter table commands
    print('1. ADD')
    print('2. DROP COLUMN')
    print('3. MODIFY COLUMN')
    
    print('\n-----------------------------------------------------------------------------------\n')

    # table selection
    alterSelection = input('Select a number: ')
    
    #add command
    if alterSelection == '1':
        showTablesDef(cnx, cursor)
        
        # table name
        table = input('Insert the name of the table to be altered: ')
        
        # column name
        condition = input('Insert the condition ADD (Condition ADD only accepts one argument. Be precise as possible with the name, data type and constraints following the example above): ')
        try:
            sqlCommand = ("ALTER TABLE {} ADD {};".format(table.upper(), condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully added {} to {} table!'.format(condition, table.upper()))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # drop column command
    elif alterSelection == '2':
        showTablesDef(cnx, cursor)
        
        # table name
        table = input('Insert the name of the table to be altered: ')
        
        # column name
        columnName = input('Insert the column name to be altered (Be precise as possible with the name following the example above): ')
        try:
            sqlCommand = ("ALTER TABLE {} DROP COLUMN {};".format(table.upper(), columnName))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully dropped column {} from {} table!'.format(columnName, table.upper()))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # modify column command
    elif alterSelection == '3':
        showTablesDef(cnx, cursor)
        
        # table name
        table = input('Insert the name of the table to be altered: ')
        
        # column name
        columnName = input('Insert the column name to be altered (Be precise as possible with the name following the example above): ')
        
        # new data type
        newDataType = input('Insert the new data type of the {} column (Be precise as possible with the data type following the example above): '.format(columnName))
        try:
            sqlCommand = ("ALTER TABLE {} MODIFY COLUMN {} {};".format(table.upper(), columnName, newDataType))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully modified column {} from {} table!'.format(columnName, table.upper()))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
