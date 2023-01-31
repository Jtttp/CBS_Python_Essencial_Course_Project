from gamers import Player, Bot, Dealer
from cards import Deck
from const import LOGO
import time


class Game:

    max_pl_count = 5

    def __init__(self):
        self.gamers = []
        self.dealer = Dealer()
        self.deck = Deck()
        self.max_bet = 10

    def add_gamers(self, count_of_bot):
        # add bot
        for _ in range(count_of_bot):
            b = Bot()
            b.get_name()
            print('\n', b.name, 'is created')
            time.sleep(1)
            b.make_bet()
            time.sleep(1)
            self.gamers.append(b)
        # add main player
        p = Player()
        p.make_bet()
        self.gamers.append(p)
        time.sleep(1)

    def first_deal(self):
        # deal two cards from the deck to each player in gamers
        for gamer in self.gamers:
            for _ in range(2):
                card = self.deck.get_card()
                gamer.take_card(card)
                time.sleep(1)
            print(gamer)
            time.sleep(1)
        # and one card to the dealer
        card = self.deck.get_card()
        self.dealer.take_card(card)
        print(self.dealer)
        time.sleep(1)
        return True

    @staticmethod
    def check_points(gamer):
        if gamer.full_points > 21:
            return True
        else:
            return False

    def taking_cards(self):
        for gamer in self.gamers:
            if isinstance(gamer, Bot):
                while gamer.full_points < 17:
                    card = self.deck.get_card()
                    gamer.take_card(card)
                    if self.check_points(gamer):
                        print(f'{gamer} BUST!')
                        time.sleep(2)
            elif isinstance(gamer, Player):
                while True:
                    asc = input('\nDo you want to take a card? (y/n) ').lower()
                    if asc == 'y':
                        card = self.deck.get_card()
                        gamer.take_card(card)
                        if self.check_points(gamer):
                            print(f'{gamer} You BUST!')
                            time.sleep(1)
                            break
                    elif asc == 'n':
                        break
                    print(gamer)
        return True

    def play_dealer(self):
        while self.dealer.full_points < 17:
            card = self.deck.get_card()
            self.dealer.take_card(card)
        print(self.dealer)

    def determine_winner(self):
        print('\n*** The final list is as follows: ***\n')
        if self.dealer.full_points > 21:
            print('The dealer bust! All players in game are win!\n')
            for gamer in self.gamers:
                if not self.check_points(gamer):
                    gamer.money += gamer.bet * 2
                    print(f'{gamer} {gamer.name} WINS {gamer.bet * 2} coins.')
                else:
                    print(f'{gamer} {gamer.name} BUST!')
        else:
            for gamer in self.gamers:
                if not self.check_points(gamer):
                    if gamer.full_points > self.dealer.full_points:
                        gamer.money += gamer.bet * 2
                        print(f'{gamer} {gamer.name} WINS {gamer.bet * 2} coins.')
                    elif gamer.full_points == self.dealer.full_points:
                        gamer.money += gamer.bet
                        print(f'{gamer} {gamer.name} WINS {gamer.bet} coins.')
                    else:
                        print(f'{gamer} {gamer.name} lost this game.')
                else:
                    print(f'{gamer} {gamer.name} BUST!')

    def start_game(self):
        try:
            while True:
                # start game
                print(LOGO)
                choice = input('Start game (y/n): ').lower()
                if choice == 'y':

                    # check new game or continue
                    if len(self.gamers) == 0:
                        print('\n*** Start a new game ***\n')
                        count_of_bot = int(input('How many bots will play? Max 4: '))
                        if count_of_bot <= 4:
                            self.add_gamers(count_of_bot)
                            Deck()
                        else:
                            print('\nIn this hand could play only four bots!')
                            self.add_gamers(count_of_bot=4)
                            Deck()
                    else:
                        print('\n*** Continue the game ***\n')
                        for gamer in self.gamers:
                            print(f'{gamer.name} continue game')
                            gamer.cards = []
                            gamer.make_bet()
                            gamer.full_points = 0
                        self.dealer.cards = []
                        self.dealer.full_points = 0
                    print('\n*** first deal ***\n')
                    self.first_deal()
                    time.sleep(1)
                    print('\n*** taking cards ***\n')
                    self.taking_cards()
                    time.sleep(1)
                    print('\n*** play with dealer ***\n')
                    self.play_dealer()
                    time.sleep(1)
                    self.determine_winner()
                elif choice == 'n':
                    break
        except KeyboardInterrupt:
            print('\nThank you for the game! ')
