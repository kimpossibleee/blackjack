from blackjack import Blackjack
from os import system, name
from time import sleep
from ascii import blackjack, deal1, deal2, deal3


class Game:
    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def deal(self):
        self.clear()
        print(deal1)
        sleep(1)
        self.clear()
        print(deal2)
        sleep(1)
        self.clear()
        print(deal3)
        sleep(2)

    def play(self):
        game_on = True
        while game_on:
            self.deal()
            self.clear()
            is_blackjack = False
            game = Blackjack()
            game.deal_new_hand()
            game.reveal_hand('user')
            game.update_score('user')
            game.print_score('user')
            print('------------vs------------')
            game.peek_dealer_hand()
            game_continue = True
            if game.user_score == 21:
                print('WOW... give me a moment...')
                sleep(2.5)
                is_blackjack = True
                game_continue = False
            while game_continue:
                print('\n')
                user_input = input('Would you like to "hit" or "stand"?: ').lower()
                self.clear()
                if 'hi' in user_input:
                    game.hit()
                    game.reveal_hand('user')
                    game.update_score('user')
                    game.print_score('user')
                    print('\n')
                    game.peek_dealer_hand()
                    if game.user_score > 21:
                        game_continue = False
                elif 'st' in user_input:
                    game_continue = False
                else:
                    print('Not a valid key. Please try again')
            self.clear()
            print('---FINAL SCORE---\n')
            if is_blackjack == True:
                print(blackjack)
            game.final_score()
            user_input = input('Press any key to continue playing, or "q" to quit: ')
            if 'q' in user_input.lower():
                print('Thanks for playing BlackJack!')
                game_on = False
