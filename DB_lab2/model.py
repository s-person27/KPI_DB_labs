import psycopg2
from psycopg2 import errors
import time
import sys


def colmn_info(table_name,column_name):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	)
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	curso_r.execute(f"SELECT {column_name} FROM {table_name}")
	print(curso_r.fetchall())
	curso_r.close()
	con.close()

def random(table_name):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	)
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	n= input("ENTER the N value : ")
	if(table_name=='author'):
		curso_r.execute(f"WITH table_m AS(INSERT INTO author SELECT chr(trunc(65+random()*25)::int), to_timestamp(1388534400+random()*63071999),chr(trunc(65 + random()*25)::int) FROM generate_series(1,{n}) RETURNING alias)INSERT INTO books SELECT alias FROM table_m")
	elif(table_name=='books'):
		curso_r.execute(f"WITH table_m AS(INSERT INTO books SELECT chr(trunc(65+random()*25)::int), chr(trunc(65 + random()*25)::int) FROM generate_series(1,{n}) RETURNING alias)INSERT INTO author SELECT alias FROM table_m")
	elif(table_name=='readers'):
		curso_r.execute(f"INSERT INTO readers SELECT chr(trunc(65+random()*25)::int), chr(trunc(65 + random()*25)::int) FROM generate_series(1,{n}) ")
	else:
		curso_r.execute(f"INSERT INTO ticket SELECT trunc(random()*1000)::int, trunc(random()*1000)::int, to_timestamp(1388534400+random()*63071999) FROM generate_series(1,{n}) ")
	curso_r.close()
	con.close()

def delete(table_name):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	column=input('Enter column : ')
	colmn_info(table_name,column)
	row=input('Enter row info : ')
	if(table_name=='author'):
		#author_v = ['alias','year_life','literary_movement']
		db_command = "WITH test AS(delete FROM author WHERE " + column + " = '"+ row + "')delete FROM books WHERE alias = '"+ row + "'"
		curso_r.execute(db_command)
		print(db_command)
	elif(table_name=='books'):
		#books_v = ['title','alias']
		db_command = "WITH test AS(delete FROM books WHERE " + column + " = '"+ row + "')delete FROM author WHERE alias = '"+ row + "'"
		curso_r.execute(db_command)
	elif(table_name=='readers'):
		#readers_v = ['name_reader','debt']
		db_command = "delete FROM readers WHERE " + column + " = '"+ row + "'"
		curso_r.execute(db_command)
	else:
		#ticket_v = ['id','cost','work_term']
		db_command = "delete FROM ticket WHERE " + column + " = '"+ row + "'"
		curso_r.execute(db_command)
	curso_r.close()
	con.close()

def add_inf(table_name):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	count=0
	mass=[]
	NULL_value = '[null]'
	if(table_name=='author'):
		print("Enter 3 value :")
		while(count<3):
			value=input()
			mass.append(value)
			count+=1
		table_name2 = 'books'
		db_command = "WITH " + table_name + " AS " + "( INSERT INTO " + table_name + " VALUES ('" + mass[0] + "','" + mass[1] + "','" + mass[2] + "'))"+ "INSERT INTO " + table_name2 + " VALUES ('" + NULL_value + "','" + mass[0] + "')"
		curso_r.execute(db_command)
	elif(table_name == 'books'):
		print("Enter 2 value :")
		while(count<2):
			value=input()
			mass.append(value)
			count+=1
		table_name2 = 'author'
		db_command = "WITH " + table_name + " AS " + "( INSERT INTO " + table_name + " VALUES ('" + mass[0] + "','" + mass[1] + "'))"+ "INSERT INTO " + table_name2 + " VALUES ('" + mass[0] + "')"
		curso_r.execute(db_command)
	elif(table_name == 'readers'): 
		print("Enter 2 value :")
		while(count<2):
			value=input()
			mass.append(value)
			count+=1
		db_command = "INSERT INTO " + table_name + " VALUES ('" + mass[0] + "','" + mass[1] + "')"
		curso_r.execute(db_command)  
	else:
		print("Enter 2 value :")
		while(count<2):
			key=input()
			mass.append(key)
			count+=1
		db_command = "INSERT INTO " + table_name + " VALUES ('" + mass[0] + "','" + mass[1] + "','" + mass[2] + "')"
		curso_r.execute(db_command)
	curso_r.close()
	con.close()

def dbl_upd(name1,name2,column):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	old_value=input('Enter old name : ')
	new_value = input('Enter new name : ')
	db_command = "WITH " + name1 + " AS (UPDATE " + name1 + " SET " + column + " = '" + new_value + "' WHERE " + column + " = '"+ old_value + "')" + " UPDATE " + name2 + " SET " + column + " = '" + new_value + "' WHERE " + column + " = '"+ old_value + "'"
	curso_r.execute(db_command)
	curso_r.close()
	con.close()

def solo_upd(name1,column):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	old_name=input('Enter old name : ')
	new_name = input('Enter new name : ')
	db_command = "UPDATE " + name1 + " SET " + column + " =  '" + new_name + "' WHERE " + column + " = '"+ old_name + "'"
	curso_r.execute(db_command)
	curso_r.close()
	con.close()

def updt(table_name):
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	column_name=input('Enter column name : ')
	colmn_info(table_name,column_name)
	if(((table_name=='author')or(table_name=='books'))and(column_name=='alias')):
		try:
			dbl_upd('author','books','alias')
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'ERROR: {err}')
	else:
		try:
			solo_upd(table_name,column_name)
		except psycopg2.Error as err:
			print(err.pgcode)
			print(f'ERROR: {err}')
	curso_r.close()
	con.close()

def Search():
	con = psycopg2.connect(
  	  database="MyData", 
  	  user="postgres", 
  	  password="", 
      host="localhost", 
  	  port="5432"
	) 
	con.set_session(autocommit=True)
	curso_r=con.cursor()
	n = input("Input quantity of attributes to search by >>> ")
	n = int(n)
	column=[]
	for h in range(0,n):
		column.append(str(input(f"Input name of the attribute number {h+1} to search by >>> ")))
	print(column)
	tables = []
	types = [] 
	if n == 2:
		curso_names_str = f"SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE information_schema.columns.column_name LIKE '{column[0]}' INTERSECT ALL SELECT table_name FROM information_schema.columns WHERE information_schema.columns.column_name LIKE '{column[1]}'"
	else:
		curso_names_str = "SELECT table_name FROM INFORMATION_SCHEMA.COLUMNS WHERE information_schema.columns.column_name LIKE '{}'".format(column[0])
	print("\ncol_names_str:", curso_names_str)
	curso_r.execute(curso_names_str)
	curso_names = (curso_r.fetchall())
	for tup in curso_names:
		tables += [tup[0]]
	if 'books/reader' in tables:
		tables.remove('books/reader')
		print(tables)
	for s in range(0,len(column)):
		for k in range(0,len(tables)):
			curso_r.execute(f"SELECT data_type FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name='{tables[k]}' AND column_name ='{column[s]}'")
			type=(curso_r.fetchall())
			for j in type:
				types+=[j[0]]
	print(types)
	if n == 1:
		if len(tables) == 1:
			if types[0] == 'character varying':
				i_char = input(f"Input string for {column[0]} to search by >>> ")
				start_time=time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}'")
				print(curso_r.fetchall())
				print("Time:%s seconds"%(time.time()-start_time))
			elif types[0] == 'integer':
				left_limits = input("Enter left limit")
				right_limits = input("Enter right limit")
				start_time=time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}'")
				print(curso_r.fetchall())
				print("Time:%s seconds"%(time.time()-start_time))
			elif types[0] == 'date':
				left_limits = input("Enter left limit date : ")
				right_limits = input("Enter right limit date : ")
				start_time=time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE date({column[0]}) BETWEEN '{left_limits}'  AND '{right_limits}'")
				print(curso_r.fetchall())
				print("Time:%s seconds"%(time.time()-start_time))

		elif len(tables) == 2:
			if types[0] == 'character varying':
				i_char = input(f"Input string for {column[0]} to search by >>> ")
				start_time = time.time()
				curso_r.execute(f"SELECT {column[0]} FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' UNION ALL SELECT {column[0]} FROM {tables[1]} WHERE {column[0]} LIKE '{i_char}'")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))

	elif n == 2:
		if len(tables) == 1:
			if types[0] == 'character varying' and types[1] == 'character varying':
				i_char = input(f"Input string for {column[0]} to search by >>> ")
				o_char = input(f"Input string for {column[1]} to search by >>> ")
				start_time = time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' AND {column[1]} LIKE '{o_char}' ")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))
			elif types[0] == 'character varying' and types[1] == 'date':
				i_char = input(f"Input string for {column[0]} to search by >>> ")
				left_limits = input(f"Enter left limit for data for {column[1]} ")
				right_limits = input(f"Enter right limit for data {column[1]} ")
				start_time = time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]} LIKE '{i_char}' AND  date({column[1]}) BETWEEN '{left_limits}' AND '{right_limits}'")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))
			elif types[0] == 'date' and types[1] == 'character varying':
				left_limits = input(f"Enter left limit for {column[0]} ")
				right_limits = input(f"Enter right limit for {column[0]} ")
				i_char = input(f"Input string for {column[1]} to search by >>> ")
				start_time = time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE date({column[0]}) BETWEEN '{left_limits}' AND '{right_limits}' AND {column[1]} LIKE '{i_char}'")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))
			elif types[0] == 'date' and types[1] == 'integer':
				left_limitsDATA = input(f"Enter left limit DATA for {column[0]} ")
				right_limitsDATA = input(f"Enter right limit DATA for {column[0]} ")
				left_limits = input(f"Enter left limit for for {column[1]} ")
				right_limits = input(f"Enter right limit for {column[1]} ")
				start_time = time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE date({column[0]}) BETWEEN '{left_limitsDATA}' AND '{right_limitsDATA}' AND {column[1]}>='{left_limits}' AND {column[1]}<'{right_limits}' ")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))
			elif types[0] == 'integer' and types[1] == 'date':
				left_limitsDATA = input(f"Enter left limit DATA for {column[1]} ")
				right_limitsDATA = input(f"Enter right limit DATA for {column[1]} ")
				left_limits = input(f"Enter left limit for {column[0]} ")
				right_limits = input(f"Enter right limit for {column[0]} ")
				start_time = time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{left_limits}' AND {column[0]}<'{right_limits}' AND date({column[1]}) BETWEEN '{left_limitsDATA}' AND '{right_limitsDATA}' ")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))
			elif types[0] == 'integer' and types[1] == 'integer':
				i_left_limits = input(f"Enter left limit for {column[0]}")
				i_right_limits = input(f"Enter right limit for {column[0]}")
				o_left_limits = input(f"Enter left limit for {column[1]}")
				o_right_limits = input(f"Enter right limit for {column[1]}")
				start_time = time.time()
				curso_r.execute(f"SELECT * FROM {tables[0]} WHERE {column[0]}>='{i_left_limits}' AND {column[0]}<'{i_right_limits}' AND {column[1]}>='{o_left_limits}' AND {column[1]}<'{o_right_limits}' ")
				print(curso_r.fetchall())
				print("Time:%s seconds" % (time.time() - start_time))
	curso_r.close()
	con.close()




