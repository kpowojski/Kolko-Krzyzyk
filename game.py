#!/usr/bin/python

PLAYER_X = []
PLAYER_O = []

turn = None

def print_game_init_screen():
	print('\n' + ' _' + '_'*70 + '\n|' + ' '*71 + '|')
	print('|\t' + '*'*60 + '\t|'  + '\n|\t' + '*'*60 + '\t|')
	print('|\t' + '*'*22 + ' KOLKO i KRZYZYK ' + '*'*21 + '\t|')
	print('|\t' + '*'*60 + '\t|'  + '\n|\t' + '*'*60 + '\t|')
	print('|' + '_'*71 + '|')


def x_sign(row_number):
	letter = '|'
	if row_number == 0:
		return letter +'   ' + letter
	elif row_number == 1:
		return ' '+ letter +' ' +letter
	elif row_number == 2:
		return '  ' + letter
	elif row_number == 3:
		return ' ' + letter + ' ' +letter
	elif row_number == 4:
		return letter +'   ' + letter

def o_sign(row_number):
	if row_number == 0: 
		return ' ' + '_'*3 + ' '
	elif row_numerb == 1:
		return '|   |'
	elif row_numerb == 2:
		return '|   |'
	elif row_numerb == 3:
		return '|   |'
	elif row_number == 4:
		return '|___|'
	
	

def game_table():
	tab = ['x', ' ',  ' ', ' ', ' ', ' ', ' ', ' ', ' ']

	for k in range(3):
		print(' '*49)
		for i in range(5):
			sign_1 = ' ' * 5
			sign_2 = ' ' * 5
			sign_3 = ' ' * 5
			
			if tab[k] is 'x':
				sign_0 = x_sign(i)
			elif tab[k+1] is 'x':
				sign_1 = x_sign(i)
			elif tab[k+2] is 'x':
				sign_2 = x_sign(i)
			elif tab[k] is 'o':
				sign_0 = o_sign(i)
			elif tab[k+1] is 'o':
				sign_1 = o_sign(i)
			elif tab[k+2] is 'o':
				sign_2 = o_sign(i)
			print('\t' + sign_0 + '\t|\t' + sign_1 + '\t|\t' + sign_2 + '\t') #normalna
		if (k <2 ):
			print ('_' * 49)
	
	
	
def validate(sign):
	if len(sign) != 1:
		return False
	if ord(sign) < 58:
		if ord(sign) > 48:
			return True
	else:
		return False

if __name__ == '__main__':
	print_game_init_screen()
	game_table()

#	while(True):
#		sign = input('Podaj pozycje na jakiej chcesz wstawic znak: ')
#		if validate(sign):
#			print('prawidlowy znak')
#			
#		else:
#			print('nieprawidlowy znak')
		

	
#Liter ma szerokość====5 i wysokość====5 	

#\t5\t|\t5\t|\t5\t  
#tabulator = 7 
	#6*7 + 2 + 3*5 = 
	#|   |
	#|   |
	#|   |
	#|___|
	       