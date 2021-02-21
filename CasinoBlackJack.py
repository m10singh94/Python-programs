import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    deck = []
    def __init__(self):
        for suit in suits:
            for rank in ranks:
                Deck.deck.append(Card(suit, rank))
    def __str__(self):
        deck_comp = ''
        for card in Deck.deck:
            deck_comp += '\n'+ card.__str__()
        return deck_comp
    def shuffle(self):
        random.shuffle(Deck.deck)
    def deal(self):
        single_card = Deck.deck.pop()
        return single_card

class Player():
    def __init__(self, bank_balance, owners_name):
        self.bank_balance = bank_balance
        self.owners_name = owners_name

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card):
        self.cards.append(card)
        self.value += value[card.rank]
        if(card.rank == 'Ace'):
            self.aces += 1
    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips do you want to bet?'))
        except:
            print('Sorry please provide an integer')
        else:
            if chips.bet > chips.total:
                print(f"You don't have that many chips. You just have {chips.total}")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing
    while playing:
        x = input("Hit or Stand? Please enter 'h' or 's':")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands... Dealer's turn")
            playing = False
        else:
            print("Invalid Input. Please enter 'h' or 's'")
            continue

def show_some(player, dealer):
    print('Dealers hand:')
    print('One card hidden')
    print(dealer.cards[1])
    print("\n")
    print("Player's hand:")
    for card in player.cards:
        print(card)
def show_all(player, dealer):
    print('Dealers hand:')
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Player's hand:")
    for card in player.cards:
        print(card)

def player_busts(player, dealer, chips):
    print("BUST Player")
    chips.lose_bet()
def player_wins(playe, dealer, chips):
    print("Player won!!")
    chips.win_bet()
def dealer_busts(player, dealer, chips):
    print('BUST Dealer')
    chips.win_bet()
def dealer_wins(player, dealer, chips):
    print('Dealer won!!')
    chips.lose_bet()
def push(player, dealer):
    print("Player and Dealer Tied. PUSH!!")

while True:
    print('Welcome to BLACKJACK')
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # to set chips
    player_chips = Chips()
    # prompt player to make bet
    take_bet(player_chips)
    # show cards
    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if(player_hand.value > 21):
            player_busts(player_hand, dealer_hand, player_chips)
            break
    if(player_hand.value <= 21):
        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)
        show_all(player_hand, dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
    print(f"\nPlayer's chips are at {player_chips.total}")
    new_game = input("Would you like to play again? (y/n)")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!!")
        break


