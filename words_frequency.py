from db_service import *
import argparse
from argparse import *
import sys



def add_word_view(word: str, pageNum: int):
    if pageNum <= 0:
        print("page number must be positive")
    if word == " ":
        print("the word is empty")

    try:
        add_word(word, pageNum)
    except Exception as e:
        print(e)

def get_pages_with_words_view(words :list):
    try:
        s = ",".join(words)
        if len(s) > 0:
            res = get_pages_by_words(s)
            print(res)
        else:
            print('please enter a string like: "x,y,z,w" ')
    except Exception as e:
        print('something went wrong: ' + e)

functionName = sys.argv[1]
if functionName == 'add_word':
    if len(sys.argv) < 4:
        print("arguments are missing")
    else:
        word = sys.argv[2]
        pageNum = sys.argv[3]
        add_word(word, pageNum)
elif functionName == 'get_pages_with_words':
    if len(sys.argv) < 3:
        print('arguments are missing')
    else:
        words = sys.argv[2]
        wordsParam = words.split(',')
        get_pages_with_words_view(wordsParam)
else:
    print('wrong function, please enter one of the following: add_word / get_pages_with_words')

