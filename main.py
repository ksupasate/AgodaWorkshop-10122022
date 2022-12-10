import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
c = conn.cursor()

# Create User Table
c.execute('''
          CREATE TABLE IF NOT EXISTS User
          ([UserEmail] TEXT PRIMARY KEY, [UserPassword] TEXT , [UserFirstname] TEXT , [UserLastname] TEXT , [UserTel] TEXT)
          ''')
# Create Property Type Table
c.execute('''
          CREATE TABLE IF NOT EXISTS PropertyType
          ([PropertyTypeId] INTEGER PRIMARY KEY, [PropertyTypeDetail] TEXT)
          ''')
# Create Property Size Tanle
c.execute('''
          CREATE TABLE IF NOT EXISTS PropertySize
          ([PropertySizeId] INTEGER PRIMARY KEY, [PropertySizeDetail] TEXT)
          ''')
# Create Property
c.execute('''
          CREATE TABLE IF NOT EXISTS Property
          ([PropertyId] INTEGER PRIMARY KEY, [PropertyName] TEXT, [PropertyTypeId] INT , [PropertySizeId] INT)
          ''')

#Get User Data
UserEmail =input('What is your UserEmail: ')
UserPassword = input('What is your UserPassword: ')
UserFirstname = input('What is your UserFirstname: ')
UserLastname = input('What is your UserLastname: ')
UserTel = input('What is your UserTel: ')

#Insert Data User
c.execute('''
          INSERT OR IGNORE INTO User (UserEmail, UserPassword, UserFirstname, UserLastname, UserTel)

                VALUES
                (
                ?,?,?,?,?
                )
          ''',
                (
                UserEmail,
                UserPassword,
                UserFirstname,
                UserLastname,
                UserTel
                ))

if(UserEmail != None):
    PropertyId =input('What is your PropertyId: ')
    PropertyName = input('What is your PropertyName: ')
    PropertyTypeId = input('What is your PropertyTypeId: ')
    PropertySizeId = input('What is your PropertySizeId: ')

    c.execute('''
          INSERT OR IGNORE INTO Property (PropertyId, PropertyName, PropertyTypeId, PropertySizeId)

                VALUES
                (
                ?,?,?,?
                )
          ''',
                (
                PropertyId,
                PropertyName,
                PropertyTypeId,
                PropertySizeId
                ))


c.execute('''
          SELECT
          *
          FROM User
          ''')
df = pd.DataFrame(c.fetchall(), columns=['UserEmail','UserPassword','UserFirstname','UserLastname','UserTel'])
print (df)
conn.commit()