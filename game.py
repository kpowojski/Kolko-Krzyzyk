#!/usr/bin/python
# -*- coding: utf-8 -*-
import collections


PLAYER_X = []
PLAYER_O = []

#table which stores all marks placed by players
#TAB = ['x', 'x',  'x', 'o', ' ', ' ', ' ', ' ', ' ']
TAB = [' '] *9
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
	else:
		return ' ' * 5

def o_sign(row_number):
	if row_number == 0: 
		return ' ' + '_'*3 + ' '
	elif row_number == 1:
		return '|   |'
	elif row_number == 2:
		return '|   |'
	elif row_number == 3:
		return '|   |'
	elif row_number == 4:
		return '|___|'
	else:
		return ' ' * 5
	

def game_table():
	
	for k in range(3):
		print(' '*49)
		for i in range(5):
			sign_0 = ' ' * 5
			sign_1 = ' ' * 5
			sign_2 = ' ' * 5
			
			if TAB[k*3] == 'x':
				sign_0 = x_sign(i)
			elif TAB[k*3] == 'o':
				sign_0 = o_sign(i)
				
			if TAB[(k*3)+1] == 'x':
				sign_1 = x_sign(i)
			elif TAB[(k*3)+1] == 'o':
				sign_1 = o_sign(i)
			
			if TAB[(k*3)+2] == 'x':
				sign_2 = x_sign(i)
			elif TAB[(k*3)+2] == 'o':
				sign_2 = o_sign(i)
			print('\t' + sign_0 + '\t|\t' + sign_1 + '\t|\t' + sign_2 + '\t') #normalna
		if (k <2 ):
			print ('_' * 49)
	
	
	
def validate(sign):
	print(len(sign))
	if len(sign) != 1:
		return False
	if ord(sign) < 57:
		if ord(sign) > 47:
			return True
	else:
		return False

def change_turn():
	global turn
	
	if turn is 'X':
		turn = 'O'
	else:
		turn = 'X'
		
		
def assign_mark(sign):
	global TAB
	print('Kolejka: {}').format(turn)
	position = int(sign, 10)
	if TAB[position] is ' ':
		TAB[position] = turn.lower()
		print('Znak {} zostal dodany do planszy na pozycji {}').format(turn, position)
	else:
		print('Pozycja zajeta, sprobuj ponownie')


def verify_result():
	winner = None
	player = turn.lower()
	
	if TAB.count(player) > 2: # postawiono co najmniej znaki danego rodzaju na planszy
		for i in range(len(TAB)):
			if i == 0 or i == 3 or i == 6:
				if TAB[i] == player and TAB[i+1] == player and TAB[i+2] == player:
					winner = player
			
			if i == 0 or i == 1 or i ==2:
				if TAB[i] == player and TAB[i+3] == player and TAB[i+6] == player:
					winner = player
			
			if i ==0:
				if TAB[i] == player and TAB[i+4] == player and TAB[i+8] == player:
					winner = player
			
			if i ==2:
				if TAB[i] == player and TAB[i+2] == player and TAB[i+4] == player:
					winner = player
	
	if TAB.count(' ') == 0 and winner == None:
		return 'END_of_GAME'
	else:
		return winner
		
		
if __name__ == '__main__':
	print_game_init_screen()
	game_table()

	turn = 'X'
	print('Gre rozpoczyna gracz {}').format(turn)
	
	while(True):
		print('Kolej gracza {}').format(turn)
		sign = raw_input('Podaj pozycje na jakiej chcesz wstawic znak: ')
		if validate(sign):
			assign_mark(sign)
			res = verify_result()
			if res == 'END_of_GAME':
				print('Koniec gry, brak zwyciezcy')
				break
			elif res != None:
				print('Zwyciezca jest: {}').format(res)
				game_table()
				break
			else:
				change_turn()
		else:
			print('Popelniles blad!\r\n\r\nProsze podac znak jeszcze raz.')
		game_table()