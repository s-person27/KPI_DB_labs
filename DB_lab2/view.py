
def Menu():
    print("If you want to update press 1")
    print("If you want to add press 2")
    print("If you want to delete press 3")
    print("If you want to random press 4")
    print("If you want to search press 5")

def OneN():
	print('There is a 1:N connection in Author and Books if the changes is in the "alias" column ,it will touch both tables :')
	print(f'author table : alias,year_life,literary_movement')
	print(f'Books table : title,alias')
def comndErr():
	print("You have to enter the command from 1 to 5 ERROR")
def tblErr():
	print('The table name is wrong ERROR')
def table_identification():
	return input('Enter table name: ')
def comand_identification():
	return input('Enter command : ')