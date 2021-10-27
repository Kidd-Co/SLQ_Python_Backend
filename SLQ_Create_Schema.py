import pymysql
import pyodbc

#Connecting to DB Server
connection = pymysql.connect(host='test-db-instance.crtop2gwcupv.us-east-2.rds.amazonaws.com',
                             user='jonny_kidd',
                             password='mypassword',
                             )

#connection = pymysql.connect(host='localhost',
#                             database='happyhabitsDB',
#                             user='root')

cursor = connection.cursor()

# Creating new DB
#sql = "drop database my_database"
#cursor.execute(sql)
#cursor.connection.commit()

sql = "create database my_database"
cursor.execute(sql)
cursor.connection.commit()

sql = "use my_database"
cursor.execute(sql)

# Creating new Table user_id
sql = '''
create table user_id (
uid int not null auto_increment,
username text,
primary key (uid)
)
'''
cursor.execute(sql)
connection.commit()

# Creating new Table habit
sql = '''
create table habit (
habitid int not null auto_increment,
description text,
happiness int,
frequency int,
last_logged text,
date_started text,
streakcounter int,
higheststreak int,
uid int,
primary key (habitid),
foreign key (uid) references user_id(uid)
)
'''
cursor.execute(sql)

connection.commit()
cursor.close()
