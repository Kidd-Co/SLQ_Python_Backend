import pymysql
import pyodbc
import constant
from datetime import date
from datetime import timedelta
import datetime

#Connecting to DB Server
connection = pymysql.connect(host='test-db-instance.crtop2gwcupv.us-east-2.rds.amazonaws.com',
                             user='jonny_kidd',
                             password='mypassword',
                             )

#connection = pymysql.connect(host='localhost',
#                             database='happyhabitsDB',
#                             user='root')

cursor = connection.cursor()

#Add new habit to database
def store_habit(description, frequency, userID):
    sql = f"""
    INSERT INTO `my_database`.`habit` 
    (`description`, `happiness`, `frequency`, `last_logged`, `date_started`, `streakcounter`, `higheststreak`, `uid`) 
    VALUES ('{description}', '{constant.STARTING_HAPPINESS}', '{frequency}', '{date.today() - timedelta(days=7)}', '{date.today()}', '1', '1', '{userID}');
    """

    cursor.execute(sql)

#return list of habits for user
def get_habits_list(userID):
    cursor.execute(f"""
    SELECT * FROM habit WHERE uid={userID};
    """)

    return cursor.fetchall()

#change habit description
def update_habit_description(habitID, new_description):
    cursor.execute(f"""
        UPDATE `my_database`.`habit`
        SET description = '{new_description}'
        WHERE habitid = {habitID};
    """)

#change habit frequency
def update_habit_frequency(habitID, new_frequency):
    cursor.execute(f"""
        UPDATE `my_database`.`habit`
        SET frequency = '{new_frequency}'
        WHERE habitid = {habitID};
    """)

#boolean function to check if habit has expired since last logged
def habit_has_expired_by(habitID, date_to_check):
    cursor.execute(f"""
       SELECT last_logged FROM `my_database`.`habit` WHERE habitid={habitID};
    """)

    last_logged = datetime.datetime.strptime(cursor.fetchall()[0][0], '%Y-%m-%d').date()

    cursor.execute(f"""
         SELECT frequency FROM `my_database`.`habit` WHERE habitid={habitID};
    """)

    frequency = cursor.fetchall()[0][0]

    return date_to_check - last_logged > timedelta(days=frequency)

#increase the happiness rank of a habit
def appreciate_habit(habitID):
    cursor.execute(f"""
         SELECT happiness FROM `my_database`.`habit` WHERE habitid={habitID};
    """)

    happiness = cursor.fetchall()[0][0]

    if happiness < constant.MAX_HAPPINESS:
        happiness = happiness + 1

    cursor.execute(f"""
           UPDATE `my_database`.`habit`
           SET happiness = '{happiness}'
           WHERE habitid = {habitID};
       """)

    print(habitID, "appreciated")

#decrease the happiness rank of a habit
def deppreciate_habit(habitID):
    cursor.execute(f"""
        SELECT happiness FROM `my_database`.`habit` WHERE habitid={habitID};
    """)

    happiness = cursor.fetchall()[0][0]

    if happiness > 0:
        happiness = happiness - 1

    cursor.execute(f"""
           UPDATE `my_database`.`habit`
           SET happiness = '{happiness}'
           WHERE habitid = {habitID};
    """)

    print(habitID, "deppreciated")

#reset streak to 0
def break_streak(habitID):
    cursor.execute(f"""
           UPDATE `my_database`.`habit`
           SET streakcounter = 0
           WHERE habitid = {habitID};
    """)

#improve habit streak and highest streak (if appropirate)
def increment_streak(habitID):
    cursor.execute(f"""
              SELECT streakcounter FROM `my_database`.`habit` WHERE habitid={habitID};
        """)

    streak = cursor.fetchall()[0][0]

    cursor.execute(f"""
             SELECT higheststreak FROM `my_database`.`habit` WHERE habitid={habitID};
        """)

    highest_streak = cursor.fetchall()[0][0]

    new_streak = streak + 1
    if new_streak > highest_streak:
        highest_streak = new_streak

    cursor.execute(f"""
           UPDATE `my_database`.`habit`
           SET streakcounter = '{new_streak}'
           WHERE habitid = {habitID};
       """)

    cursor.execute(f"""
           UPDATE `my_database`.`habit`
           SET higheststreak = '{highest_streak}'
           WHERE habitid = {habitID};
       """)

#update habit as if acted on today
def action_habit(habitID):
    cursor.execute(f"""
        UPDATE `my_database`.`habit`
        SET last_logged = '{date.today()}'
        WHERE habitid = {habitID};
    """)

    increment_streak(habitID)
