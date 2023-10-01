# imports
import sys
from config.configuration import MySql
from functions.showtables import showTablesDef
from functions.insert import insertDef
from functions.delete import deleteDef
from functions.update import updateDef
from functions.createtable import createTableDef
from functions.createview import createViewDef
from functions.alter import alterDef
from functions.query import queryDef

# main function
def main():
    
    #  main login interface
    print('\n--------------- MySQL Login ---------------\n')
    print('User (root): root')
    myPassword = input('Password: ')
    print('Host: localhost')
    print('Database: ART_OBJECT')
    print('\n-------------------------------------------\n')
    
    # connection and cursor init
    myUser = MySql(myPassword)
    cnx = myUser.myConnection()
    
    try:
        cursor = cnx.cursor()
    except:
        sys.exit('Error: User does not exist.\n')
    
    # interface
    while True:
        
        # show tables
        showTablesDef(cnx, cursor)
        
        # sql command interface
        print('--------------- Select SQL Command ---------------\n')
        print('1. INSERT')
        print('2. DELETE')
        print('3. UPDATE')
        print('4. CREATE TABLE')
        print('5. CREATE VIEW')
        print('6. ALTER')
        print('7. QUERY')
        print('8. Exit')
        print('\n---------------------------------------------------\n')
        
        # main interface selection
        mainSelection = input('Select a number: ')

        # insert command interface
        if mainSelection == '1':
            insertDef(cnx, cursor)
        
        # delete command interface
        elif mainSelection == '2':
            deleteDef(cnx, cursor)
        
        # update command interface
        elif mainSelection == '3':
            updateDef(cnx, cursor)
            
        # create table command interface
        elif mainSelection == '4':
            createTableDef(cnx, cursor)
        
        # create view command interface
        elif mainSelection == '5':
            createViewDef(cnx, cursor)
            
        # alter command interface
        elif mainSelection == '6':
            alterDef(cnx, cursor)
            
        # query command interface
        elif mainSelection == '7':
            queryDef(cnx, cursor)
        
        # exit
        elif mainSelection == '8':
            print('\n--------------- Exiting... ---------------\n')
            cnx.close()
            break

# init
if __name__ == '__main__':
    main()