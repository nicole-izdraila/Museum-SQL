# imports
import mysql.connector
from mysql.connector import errorcode


# insert function
def insertDef(cnx, cursor):
    print('\n--------------- Select Table to use SQL command INSERT -----------------\n')
    
    # example of the sql command
    print('To use the INSERT SQL Command follow the example below.\n')
    print('***************** EXAMPLE *******************\n')
    print("INSERT INTO PERSONS(PersonID, FName, LName)\nVALUES(1, 'Axel', 'Sanchez')")
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
    insertSelection = input('Select a number: ')
            
    # ART table
    if insertSelection == '1':
        print('\n--------------- ART Table ---------------\n')
        ID_Num = input('Insert ID_Num -> data type INT: ')
        Title = input('Insert Title -> data type VARCHAR(30): ')
        YearCreated = input('Insert YearCreated -> data type VARCHAR(30): ')
        Descr = input('Insert Descr -> data type VARCHAR(100): ')
        Origin = input('Insert Origin -> data type VARCHAR(30): ')
        Name_ = input('Insert Name_ -> data type VARCHAR(30): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO ART(ID_Num, Title, YearCreated, Descr, Origin, Name_) VALUES(%s, %s, %s, %s, %s, %s)')
            cursor.execute(sqlCommand, (ID_Num, Title, YearCreated, Descr, Origin, Name_))
            cnx.commit()
            print('Successfully inserted into ARTIST({}, {}, {}, {}, {}, {})!'.format(ID_Num, Title, YearCreated, Descr, Origin, Name_))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # ARTIST table
    if insertSelection == '2':
        print('\n--------------- ARTIST Table ---------------\n')
        Name = input('Insert Name -> data type VARCHAR(40): ')
        CountryOrigin = input('Insert CountryOrigin -> data type VARCHAR(40): ')
        MainStyle = input('Insert MainStyle -> data type VARCHAR(40): ')
        Epoch = input('Insert Epoch -> data type VARCHAR(40): ')
        Descr = input('Insert Descr -> data type VARCHAR(100): ')
        DateBorn = input('Insert DateBorn -> data type INT: ')
        DateDied = input('Insert DateDied -> data type INT: ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO ARTIST(Name, CountryOrigin, MainStyle, Epoch, Descr, DateBorn, DateDied) VALUES(%s, %s, %s, %s, %s, %s, %s)')
            cursor.execute(sqlCommand, (Name, CountryOrigin, MainStyle, Epoch, Descr, DateBorn, DateDied))
            cnx.commit()
            print('Successfully inserted into ARTIST({}, {}, {}, {}, {}, {}, {})!'.format(Name, CountryOrigin, MainStyle, Epoch, Descr, DateBorn, DateDied))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))

    # BORROWED table
    elif insertSelection == '3':
        print('\n--------------- BORROWED Table ---------------\n')
        ID_Num = input('Insert ID_Num -> data type INT: ')
        DateBorrowed = input('Insert DateBorrowed -> data type VARCHAR(30): ')
        DateReturned = input('Insert DateReturned -> data type VARCHAR(30): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO BORROWED(ID_Num, DateBorrowed, DateReturned) VALUES(%s, %s, %s)')
            cursor.execute(sqlCommand, (ID_Num, DateBorrowed, DateReturned))
            cnx.commit()
            print('Successfully inserted into BORROWED({}, {}, {})!'.format(ID_Num, DateBorrowed, DateReturned))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            
    # COLLECTION table    
    elif insertSelection == '4':
        print('\n--------------- COLLECTION Table ---------------\n')
        COLL_Name = input('Insert COLL_Name -> data type VARCHAR(100): ')
        Descr = input('Insert Descr -> data type VARCHAR(100): ')
        Phone = input('Insert Phone -> data type INT: ')
        Contact = input('Insert Contact -> data type VARCHAR(30): ')
        print('\n----------------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO COLLECTION(COLL_Name, Descr, Phone, Contact) VALUES(%s, %s, %s, %s)')
            cursor.execute(sqlCommand, (COLL_Name, Descr, Phone, Contact))
            cnx.commit()
            print('Successfully inserted into COLLECTION({}, {}, {}, {})!'.format(COLL_Name, Descr, Phone, Contact))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # EXHIBITION table
    elif insertSelection == '5':
        print('\n--------------- EXHIBITION Table ---------------\n')
        ID_Num = input('Insert ID_Num -> data type INT: ')
        EXH_Name = input('Insert EXH_Name -> data type VARCHAR(50): ')
        StartDate = input('Insert StartDate -> data type VARCHAR(30): ')
        EndDate = input('Insert EndDate -> data type VARCHAR(30): ')
        print('\n---------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO EXHIBITION(ID_Num, EXH_Name, StartDate, EndDate) VALUES(%s, %s, %s, %s)')
            cursor.execute(sqlCommand, (ID_Num, EXH_Name, StartDate, EndDate))
            cnx.commit()
            print('Successfully inserted into EXHIBITION({}, {}, {}, {})!'.format(ID_Num, EXH_Name, StartDate, EndDate))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # OTHER table
    elif insertSelection == '6':
        print('\n--------------- OTHER Table ---------------\n')
        ID_Num = input('Insert ID_Num -> data type INT: ')
        Style = input('Insert Style -> data type VARCHAR(30): ')
        TypeDescr = input('Insert TypeDescr -> data type VARCHAR(10): ')
        print('\n--------------------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO OTHER(ID_Num, Style, TypeDescr) VALUES(%s, %s, %s)')
            cursor.execute(sqlCommand, (ID_Num, Style, TypeDescr))
            cnx.commit()
            print('Successfully inserted into OTHER({}, {}, {})!'.format(ID_Num, Style, TypeDescr))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # PAINTING table
    elif insertSelection == '7':
        print('\n--------------- PAINTING Table ---------------\n')
        ID_Num = input('Insert ID_Num -> data type INT: ')
        PaintType = input('Insert PaintType -> data type VARCHAR(25): ')
        Material = input('Insert Material -> data type VARCHAR(30): ')
        print('\n--------------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO PAINTING(ID_Num, PaintType, Material) VALUES(%s, %s, %s)')
            cursor.execute(sqlCommand, (ID_Num, PaintType, Material))
            cnx.commit()
            print('Successfully inserted into PAINTING({}, {}, {})!'.format(ID_Num, PaintType, Material))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # PERMANENT table
    elif insertSelection == '8':
        print('\n--------------- PERMANENT Table ---------------\n')
        ID_Num = input('Insert ID_Num -> data type INT: ')
        DateAcquired = input('Insert DateAcquired -> data type VARCHAR(30): ')
        CurrentStatus = input('Insert CurrentStatus -> data type VARCHAR(30): ')
        print('\n-------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO PERMANENT(ID_Num, DateAcquired, CurrentStatus, Member3) VALUES(%s, %s, %s)')
            cursor.execute(sqlCommand, (ID_Num, DateAcquired, CurrentStatus))
            cnx.commit()
            print('Successfully inserted into PERMANENT({}, {}, {})!'.format(ID_Num, DateAcquired, CurrentStatus))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            
    # SCULPTURE table
    elif insertSelection == '9':
        print('\n--------------- SCULPTURE Table ---------------\n')
        ID_Num = input('Insert ID_Num -> data type INT: ')
        Style = input('Insert Style -> data type VARCHAR(30): ')
        Weight = input('Insert Weight -> data type VARCHAR(10): ')
        Height = input('Insert Height -> data type VARCHAR(10): ')
        Material = input('Insert Material -> data type VARCHAR(25): ')
        print('\n--------------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO SCULPTURE(ID_Num, Style, Weight, Height, Material) VALUES(%s, %s, %s, %s, %s)')
            cursor.execute(sqlCommand, (ID_Num, Style, Weight, Height, Material))
            cnx.commit()
            print('Successfully inserted into SCULPTURE({}, {}, {}, {}, {})!'.format(ID_Num, Style, Weight, Height, Material))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
    
    # STATUE table
    elif insertSelection == '10':
        print('\n--------------- STATUE Table ---------------\n')
        ID_Num = input('Insert ID_Num -> data type INT: ')
        Style = input('Insert Style -> data type VARCHAR(30): ')
        Weight = input('Insert Weight -> data type VARCHAR(10): ')
        Height = input('Insert Height -> data type VARCHAR(10): ')
        Material = input('Insert Material -> data type VARCHAR(25): ')
        print('\n--------------------------------------------------\n')
        try:
            sqlCommand = ('INSERT INTO STATUE(ID_Num, Style, Weight, Height, Material) VALUES(%s, %s, %s, %s, %s)')
            cursor.execute(sqlCommand, (ID_Num, Style, Weight, Height, Material))
            cnx.commit()
            print('Successfully inserted into STATUE({}, {}, {}, {}, {})!'.format(ID_Num, Style, Weight, Height, Material))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))