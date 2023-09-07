import sqlite3

conn = sqlite3.connect('data.db' , check_same_thread=False)
cursor = conn.cursor()

def adding_user_to_data_base(user_id: int, chat_id : int , user_name: str, user_surname: str):
	cursor.execute('INSERT INTO users (user_id, chat_id, user_name, user_surname) VALUES (?, ?, ?, ?)', (user_id, chat_id, user_name, user_surname))
	conn.commit()

sqlite_select_query = """SELECT * from users"""

def chesk_user_into_database(user_id : int , chat_id : int):
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if row[1] == user_id and row[4] == chat_id :
            return False
    return True

def user_check(user_id: int, chat_id : int , user_name: str, user_surname: str):
    is_user = chesk_user_into_database(user_id , chat_id)
     
    if is_user:
        adding_user_to_data_base(user_id , chat_id , user_name , user_surname)
        message = 'User sucsesfuly added to database'
        return message
    else :
        message = 'User found in databade'
        return message
def gat_all_users ():
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    return records
# adding_user_to_data_base(1000 , 1221 , 'Behruz' , 'Begmatov')
# print(user_check(user_id=2003 , chat_id=133 , user_name='Test' , user_surname='FOOOOO'))