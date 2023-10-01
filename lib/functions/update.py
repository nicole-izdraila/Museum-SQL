# imports
import mysql.connector
from mysql.connector import errorcode


# update function
def updateDef(cnx, cursor):
    print('\n--------------- Select Table to use SQL command UPDATE -----------------\n')
    
    # example of the sql command
    print('To use the UPDATE SQL Command follow the example below.\n')
    print('***************** EXAMPLE *******************\n')
    print("UPDATE PERSONS\nSET FName = 'Axel', LName = 'Sanchez'\nWHERE PersonID = 1 OR PersonID = 4;")
    print('\n*********************************************\n')
    
    # tables
    print('1. ART')
    print('2. ARTIST')
    print('3. BORROWED')
    print('4. COLLECTION')
    print('5. EXHIBITION')
    print('6. OTHER')
    print('7. PAINTING')
    print('8. PERMANENT')
    print('9. SCULPTURE')
    print('10. STATUE')
    
    print('\n------------------------------------------------------------------------\n')
    
    # table selection
    updateSelection = input('Select a number: ')
    
    # ART table
    if updateSelection == '1':
        print('\n--------------- ART Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE ART SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # ARTIST table
    elif updateSelection == '2':
        print('\n--------------- ARTIST Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE ARTIST SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))

    # BORROWED table
    elif updateSelection == '3':
        print('\n--------------- BORROWED Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE BORROWED SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            
    # COLLECTION table    
    elif updateSelection == '4':
        print('\n--------------- COLLECTION Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE COLLECTION SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # EXHIBITION table
    elif updateSelection == '5':
        print('\n--------------- EXHIBITION Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE EXHIBITION SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # OTHER table
    elif updateSelection == '6':
        print('\n--------------- OTHER Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE OTHER SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # PAINTING table
    elif updateSelection == '7':
        print('\n--------------- PAINTING Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE PAINTING SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # PERMANENT table
    elif updateSelection == '8':
        print('\n--------------- PERMANENT Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE PERMANENT SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            
    # SCULPTURE table
    elif updateSelection == '9':
        print('\n--------------- SCULPTURE Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE SCULPTURE SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # STATUE table
    elif updateSelection == '10':
        print('\n--------------- STATUE Table ---------------\n')
        sets = input('Insert the condition SET to be updated (Use comma after every statement. Be precise as possible following the example above): ')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('UPDATE STATUE SET {} WHERE {};'.format(sets, condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully updated the SET {}!'.format(sets))
            print(cursor.rowcount, "record(s) affected")
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))