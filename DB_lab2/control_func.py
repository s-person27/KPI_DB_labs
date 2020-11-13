import psycopg2
from psycopg2 import errors
from model import * 
from view import *


author_v = ['alias','year_life','literary_movement']
books_v = ['title','alias']

def request():

    input_command=input('Enter command : ')
    if(input_command=='5'):
        try:
            if(input_command=='5'):
                Search()
                sys.exit()
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'ERROR: {err}')  
    table=input('Enter table name : ')
    if((table =='author')or(table=='books')):
        print('There is a 1:N connection in Author and Books if the changes is in the "alias" column ,it will touch both tables :')
        print(f'author table : {author_v}')
        print(f'Books table : {books_v}')
        try:
            if(input_command=='1'):
                updt(table)
            elif(input_command=='2'):
                add_inf(table)
            elif(input_command=='3'):
                delete(table)
            elif(input_command=='4'):
                random(table)
            elif(input_command != '5'or'4'or'3'or'2'or'1'):
                print("Error: wrong command, it has to be from 1 to 5")  
                sys.exit()
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'ERROR: {err}')
    elif((table=='readers')or(table=='ticket')):
        try:
            if(input_command=='1'):
                updt(table)
            elif(input_command=="2"):
                add_inf(table)
            elif(input_command=='3'):
                delete(table)
            elif(input_command=='4'):
                random(table)
            elif(input_command != '5'or'4'or'3'or'2'or'1'):
                print("You have to enter the command from 1 to 5 ERROR")  
                sys.exit()
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'ERROR: {err}')
    else:
        print('The table name is wrong ERROR')

Menu()  
request()
