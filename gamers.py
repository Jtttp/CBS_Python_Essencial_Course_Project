import abc
import random
from const import MAX_BET, NAME


class AbcGamer(abc.ABC):

    def __init__(self):
        self.name = None
        self.cards = []
        self.bet = 0
        self.full_points = 0
        self.money = 100

    def __str__(self):
        message = f'Bet: {str(self.bet)} Points {str(self.full_points)}'
        print(message)

    def take_card(self, card):
        self.cards.append(card)
        self.full_points += card.point

    def get_name(self):
        pass

    def make_bet(self):
        pass


class Player(AbcGamer):
    def __init__(self):
        super().__init__()
        self.name = str(input('\nPlease input your name: ')).title()

    def __str__(self):
        message = f"{self.name} has next cards: ({', '.join([str(x) for x in [*self.cards]])}) " \
                  f"Points: {str(self.full_points)}."
        return message

    def make_bet(self):
        while True:
            bet = int(input(f'\nPlace your bets please (max bet is {MAX_BET}): '))
            if bet <= 10:
                self.bet = bet
                self.money -= self.bet
                print(f'{self.name}\'s bet is: ', self.bet)
                break
            else:
                print(f'Max bet on this table is {MAX_BET}')
                self.bet = 10
                print(f'{self.name} bet in this hand is: ', self.bet)
                break


class Bot(AbcGamer):
    def __init__(self):
        super().__init__()

    def __str__(self):
        message = f"{self.name} has next cards: ({', '.join([str(x) for x in [*self.cards]])}) " \
                  f"Points: {str(self.full_points)}.\n"
        return message

    def make_bet(self):
        self.bet = random.randint(1, MAX_BET)
        self.money -= self.bet
        print(f'{self.name}`s bet is: {self.bet}')

    def get_name(self):
        self.name = NAME.pop(random.randint(0, len(NAME)-1))


class Dealer(AbcGamer):
    def __init__(self):
        super().__init__()

    def __str__(self):
        message = f"\nDealer`s cards: ({','.join([str(x) for x in [*self.cards]])}) " \
                  f"Points: {str(self.full_points)}."
        return message
