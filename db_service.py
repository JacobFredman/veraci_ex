import mysql.connector
from mysql.connector import errorcode
from config import *


def get_pages_by_words(words: str):
    if len(words) == 0:
        raise Exception("the list must not be empty")

    try:
        conn = mysql.connector.connect(**connDict)
        conn._open_connection()
        cursor = conn.cursor()
        cursor.callproc('get_pages_with_words', (words,))
        result_array = []
        for result in cursor.stored_results():
            result_array = [x[0] for x in result.fetchall()] 
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with connection to DB")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        conn.close()
    return result_array


def add_word(word: str, pageNum: int):
    if word == '':
        raise Exception("the word must not be empty")

    try:
        conn = mysql.connector.connect(**connDict)
        conn._open_connection()
        cursor = conn.cursor()
        cursor.callproc('add_word', (word,pageNum))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with connection to DB")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        conn.close()

