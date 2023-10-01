# imports
import mysql.connector
from mysql.connector import errorcode


# delete function
def deleteDef(cnx, cursor):
    print('\n--------------- Select Table to use SQL command DELETE -----------------\n')
    
    # example of the sql command
    print('To use the DELETE SQL Command follow the example below.\n')
    print('***************** EXAMPLE *******************\n')
    print("DELETE FROM PERSONS\nWHERE PersonID = 1")
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
    print('11. Delete a specific table')
    
    print('\n------------------------------------------------------------------------\n')
    
    # table selection
    deleteSelection = input('Select a number: ')
    
    # ART table
    if deleteSelection == '1':
        print('\n--------------- ART Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM ART WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from ART table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # ARTIST table        
    elif deleteSelection == '2':
        print('\n--------------- ARTIST Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n-------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM ARTIST WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from ARTIST table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))

    # BORROWED table
    elif deleteSelection == '3':
        print('\n--------------- BORROWED Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM BORROWED WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from BORROWED table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # COLLECTION table            
    elif deleteSelection == '4':
        print('\n--------------- COLLECTION Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n----------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM COLLECTION WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from COLLECTION table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # EXHIBITION table            
    elif deleteSelection == '5':
        print('\n--------------- EXHIBITION Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM EXHIBITION WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from EXHIBITION table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # OTHER table            
    elif deleteSelection == '6':
        print('\n--------------- OTHER Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n--------------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM OTHER WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from OTHER table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # PAINTING table            
    elif deleteSelection == '7':
        print('\n--------------- PAINTING Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n--------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM PAINTING WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from PAINTING table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # PERMANENT table            
    elif deleteSelection == '8':
        print('\n--------------- PERMANENT Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n-------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM PERMANENT WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from PERMANENT table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # SCULPTURE table        
    elif deleteSelection == '9':
        print('\n--------------- SCULPTURE Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n--------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM SCULPTURE WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from SCULPTURE table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # STATUE table        
    elif deleteSelection == '10':
        print('\n--------------- STATUE Table ---------------\n')
        condition = input('Insert condition WHERE (Condition WHERE accepts multiple arguments separated by AND/OR. Be precise as possible following the example above): ')
        print('\n--------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM STATUE WHERE {};'.format(condition))
            cursor.execute(sqlCommand)
            cnx.commit()
            print('Successfully deleted from STATUE table where {}!'.format(condition))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            
    # ART_OBJECT database
    elif deleteSelection == '11':
        print('\n--------------- ART_OBJECT Database ---------------\n')
        table = input('Insert the name of the table to delete all records on it (Be precise as possible): ')
        print('\n-------------------------------------------------------\n')
        try:
            sqlCommand = ('DELETE FROM {};'.format(table.upper()))
            cursor.execute(sqlCommand)
            print('Successfully dropped {} table!'.format(table.upper()))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))