# imports
import mysql.connector
from mysql.connector import errorcode
from functions.showtables import showTablesDef


# create view function
def createViewDef(cnx, cursor):
    print('\n--------------- Select Table to use SQL command CREATE VIEW -----------------\n')
    
    # example of the sql command
    print('To use the CREATE VIEW SQL Command follow the example below.\n')
    print('***************** EXAMPLE *******************\n')
    print("CREATE VIEW MEN AS\nSELECT *\nFROM PERSONS\nWHERE Sex = 'M' OR BirthYear > 2000;")
    print('\n*********************************************\n')
    
    # view variable
    view = input('Insert the name of the view: ')
    
    showTablesDef(cnx, cursor)
    
    # table name
    table = input('Insert the name of the table: ')
    
    # selection statement
    select = input('Insert the condition SELECT to be updated (Use comma after every statement or use * to select all. Be precise as possible following the example above): ')
    
    # where condition
    condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
    print('\n-----------------------------------------------------------------------------\n')

    try:
        sqlCommand = ('CREATE VIEW {} AS SELECT {} FROM {} WHERE {};'.format(view.upper(), select, table.upper(), condition))
        cursor.execute(sqlCommand)
        cnx.commit()
        print('Successfully created view {} from {}!'.format(view, table))
    except mysql.connector.Error as err:
        print('Error: {}'.format(err))
