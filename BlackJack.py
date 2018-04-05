'''
 This is a game of BlackJack.
 The computer is the dealer and the user will be the player.
'''

import random


class Player():
	"""docstring for Player"""
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		self.stay = False
		self.hand = []
		self.bet_amount = 0

	def bet(self, amount):
		self.bet_amount = amount

	def hit(self):
		self.hand.append(deal())

	def stand(self):
		self.stay = True
		
	def show_cards(self):
		print ('\n' + self.name + "'s hand:")
		print (' '.join(str(x) for x in self.hand))
		
	def total_of_hand(self):
		if not 'A' in self.hand:
			return sum(self.hand)
		else:
			#A is in the hand
			total = 0
			count_A = 0
			for card in self.hand:
				if card == 'A':
					count_A += 1
					continue
				elif card in ['J','Q','K']:
					total +=  10
				else:
					total += card
			total_of_other_cards = total
			if count_A == 1:
				# if we consider 'A' to be 11
				if total_of_other_cards + 11 <=21:
					return total_of_other_cards + 11
				else:
					return total_of_other_cards + 1
			else:
				if total_of_other_cards + 11 + count_A-1 <=21:
					return total_of_other_cards + 11 + count_A-1
				else:
					return total_of_other_cards + count_A
			
	def check_for_bust(self):
		return self.total_of_hand() > 21
	
	def deduct_bet_amount(self):
		self.balance -= self.bet_amount
		print ('remaining funds= {}'.format(self.balance))
		
	def reward_player(self):
		self.balance += self.bet_amount


class Dealer():
	"""docstring for Dealer"""
	def __init__(self):
		self._hidden_card = None
		self.hand = []
		self.stay = False

	def hit(self):
		self.hand.append(deal())
		if len(self.hand) == 1:
			self._hidden_card = self.hand[0]
			self.hand[0] = '*'

	def turn_up_card(self):
		self.hand[0] = self._hidden_card
		
	def show_cards(self):
		print ("\ndealer's hand:")
		print (' '.join(str(x) for x in self.hand))
		
	def total_of_hand(self):
		if not 'A' in self.hand:
			return sum(self.hand)
		else:
			#A is in the hand
			total = 0
			count_A = 0
			for card in self.hand:
				if card == 'A':
					count_A += 1
					continue
				elif card in ['J','Q','K']:
					total +=  10
				else:
					total += card
			total_of_other_cards = total
			if count_A == 1:
				# if we consider 'A' to be 11
				if total_of_other_cards + 11 > 16 and total_of_other_cards + 11 <=21:
					return total_of_other_cards + 11
				else:
					return total_of_other_cards + 1
			else:
				if total_of_other_cards + 11 + count_A-1 > 16 and total_of_other_cards + 11 + count_A-1 <=21:
					return total_of_other_cards + 11 + count_A-1
				else:
					return total_of_other_cards + count_A
	
	def check_for_bust(self):
		return self.total_of_hand() > 21
	

def deal():
	card = cards.pop()
	if not card == 'A':
		return card_dict[card]
	else:
		return card

def get_bet_amount(p):
	while True:
		bet_amt = int(input('Enter the amount you would like to bet'))
		if bet_amt > p.balance:
			print('Insufficient funds to place this bet')
			continue
		else:
			p.bet(bet_amt)
			break

def deal_initial_cards(p,d):
	p.hit()
	p.hit()
	p.show_cards()
	
	d.hit()
	d.hit()
	d.show_cards()

def check_for_end_of_game(p,d):
	if p.check_for_bust() and not d.check_for_bust():
		print ('Player busted and dealer did not bust')
		print ('The Dealer wins')
		p.deduct_bet_amount()
	elif p.check_for_bust() and d.check_for_bust():
		print('Both player and dealer busted')
		print('The game has ended in a draw')
	elif not p.check_for_bust() and d.check_for_bust():
		print('Player did not bust but dealer busted')
		print('{} wins'.format(p.name))
		p.reward_player()
	elif not p.check_for_bust()and not d.check_for_bust():
		print ('Both Player and dealer did not bust')
		if p.total_of_hand() > d.total_of_hand():
			print("player's hand is more than the dealer's hand")
			print('{} wins'.format(p.name))
			p.reward_player()
		elif p.total_of_hand() < d.total_of_hand():
			print("dealer's hand is more than the player's hand")
			p.deduct_bet_amount()
			print ('Dealer wins!')
		else:
			print ('Both player and dealer have the same value...Game is a tie!')
	print ("Remaining amount left with {} is {}.".format(p.name,p.balance))
			
def start():
	print ('Welcome to the Bellagio. Let us play a game of BlackJack')
	player_name, balance = input('Enter your name and the cost of chips you would like to buy')
	P = Player(player_name, balance)
	D = Dealer()
	print ('Let us begin the game. Good luck!')
	start_game(P,D)

def start_game(player1, dealer):
	get_bet_amount(player1)
	deal_initial_cards(player1,dealer)
	#time for player to starting hitting if he wants
	while True:
		answer = str(raw_input("Would you like to hit? (enter 'y' or 'n')"))
		print (answer)
		if answer.lower() not in ['y', 'n']:
			print ("Please enter 'y' or 'n' only")
			continue
		if answer.lower() == 'y':
			player1.hit()
		elif answer.lower() == 'n':
			player1.stand()
			break
		player1.show_cards()
		if player1.check_for_bust():
			print ('{} has busted.'.format(player1.name))
			break
	#time for dealer to hit if he wants
	dealer.turn_up_card()
	dealer.show_cards()
	while not dealer.total_of_hand() > 16:
		dealer.hit()
		dealer.show_cards()
	dealer.stay = True
	check_for_end_of_game(player1,dealer)
	if player1.balance > 0:
		
		while True:
			answer =  str(raw_input("Would you like to play another game? (enter 'y' on 'n')"))
			if answer.lower() in ['y','n']:
				if answer == 'y':
					player1.hand = []
					dealer.hand = []
					start_game(player1, dealer)
				else:
					print ('Thank you for playing BlackJack!')
				break
			else:
				print ('Please enter a valid option')
				continue
	else:
		print ('Thank you for playing BlackJack!')



cards = 4 * ['two','three','four','five','six','seven','eight','nine','ten','J','Q','K','A']
random.shuffle(cards)
card_dict = {'two':2 , 'three':3 , 'four':4 , 'five':5 , 'six':6 , 'seven':7 , 'eight':8 , 'nine':9 , 'ten':10 , 'J':10 , 'Q':10 , 'K':10}
start()

