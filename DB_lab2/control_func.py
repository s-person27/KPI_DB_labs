import psycopg2
from psycopg2 import errors
from model import * 
from view import *
import sys


def request():

    input_command = comand_identification()
    if(input_command=='5'):
        try:
            if(input_command=='5'):
                Search()
                sys.exit()
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'ERROR: {err}')  
    table=table_identification()
    if((table =='author')or(table=='books')):
        OneN()
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
                comndErr()  
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
                comndErr()  
                sys.exit()
        except psycopg2.Error as err:
            print(err.pgcode)
            print(f'ERROR: {err}')
    else:
        tblErr()

Menu()  
request()
