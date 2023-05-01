import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}'

class Deck:
    SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
    VALUES = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    def __init__(self):
        self.deck = [Card(suit, value)for suit in Deck.SUITS for value in Deck.VALUES]

    def size(self):
        return len(self.deck)
# SHUFFLE THE DECK
    def shuffle(self):
        random.shuffle(self.deck)
# LOOK AT THE TOP CARD
    def peek(self):
        peek_card = Card(self.deck[-1][1],  self.deck[-1][0])
        return peek_card
# REMOVE A CARD FROM THE DECK WHEN DRAWN
    def draw(self):
        removed_card = self.deck.pop()
        return removed_card
# RESET THE DECK TO A BRAND NEW DECK
    def reset(self) -> None:
        self.deck = [Card(value, suit)for suit in Deck.SUITS for value in Deck.VALUES]
        self.shuffle()

class Blackjack:
    def __init__(self):
        self.current_deck = Deck()
        self.user_hand = []
        self.dealer_hand = []
        self.discard_pile = []
        self.user_score = 0
        self.dealer_score = 0
        self.is_blackjack = False

    def deal_new_hand(self):
        self.current_deck.shuffle()
# initially deals two cards to both the player and dealer
        for i in range(2):
            self.user_hand.append(self.current_deck.draw())
            self.dealer_hand.append(self.current_deck.draw())

    def hit(self):
        if self.current_deck.size() < 1:
            game_continue = False
            print('No more cards left to deal. Please restart the game')

        else:
            self.user_hand.append(self.current_deck.draw())

    def peek_dealer_hand(self):
        print(f'DEALER HAND: [{self.dealer_hand[0]}], [HIDDEN]')

    def reveal_hand(self, user_or_dealer):
        if user_or_dealer.upper() == 'USER':
            hand = self.user_hand
        else:
            hand = self.dealer_hand
        list_of_cards = ''
        for card in hand:
            list_of_cards += f'[{card}], '
        print(f'{user_or_dealer.upper()} HAND: {list_of_cards}')

    def update_score(self, user_or_dealer):
        if user_or_dealer.upper() == 'USER':
            hand = self.user_hand
        else:
            hand = self.dealer_hand
        has_ace = False
        score = 0
        for card in hand:
            if card.value in ("Jack", "Queen", "King"):
                score += 10
            elif card.value == 'Ace':
                score += 11
                has_ace = True
            else:
                score += card.value
        if has_ace == True and score > 21:
            score -= 10
        if user_or_dealer.upper() == 'USER':
            self.user_score = score
        else:
            self.dealer_score = score
        return score

    def deal_hit(self):
        self.update_score('dealer')
        while self.dealer_score < 17 and self.user_score < 21:
            self.dealer_hand.append(self.current_deck.draw())
            self.update_score('dealer')

    def print_score(self, user_dealer):
        if user_dealer == 'user':
            score = self.user_score
        else:
            score = self.dealer_score
        print(f'{user_dealer.upper()} SCORE: {score}')

    def reshuffle(self):
        self.current_deck.reset()
        self.discard_pile = []
        self.user_hand = []
        self.dealer_hand = []

    def final_score(self):

        self.deal_hit()
        self.reveal_hand('user')
        self.print_score('user')
        print('------------vs------------')
        self.reveal_hand('dealer')
        self.print_score('dealer')
        print('\n')

        if len(self.user_hand) == 2 and self.user_score == 21:
            self.is_blackjack = True

        if self.user_score == self.dealer_score and self.is_blackjack == False:
            print('Draw')
        elif self.user_score > 21:
            print('BUST!! You lose :(')
        elif self.dealer_score > 21 or self.user_score > self.dealer_score:
            print('You WIN!')
        elif self.dealer_score > self.user_score:
            print('You LOSE.')
        print('\n')
