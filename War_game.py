import random

SUITE = ['Serduszko', 'Wino', 'Żołądź', 'Dzwonek']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JOPEK', 'DAMA', 'KROL', 'AS']


class Hand:
    def __init__(self):
        self.card_deck = self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        deck = []
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                       '8': 8, '9': 9, '10': 10, 'JOPEK': 11, 'DAMA': 12, 'KROL': 13, 'AS': 14}
        for suite in range(len(SUITE)):
            for rank in range(len(RANKS)):
                value = card_values[RANKS[rank]]
                card = {'suite': SUITE[suite],
                        'rank': RANKS[rank], 'value': value}
                deck.append(card)
        return deck

    def shuffle_deck(self):
        random.shuffle(self.card_deck)

    def deal_cards(self):
        half = len(self.card_deck) // 2
        player_hand = self.card_deck[:half]
        computer_hand = self.card_deck[half:]
        return player_hand, computer_hand


hand = Hand()

player_hand, computer_hand = hand.deal_cards()


class Game:
    def __init__(self, player_hand, computer_hand):
        self.player_hand = player_hand
        self.computer_hand = computer_hand
        self.table_cards = []

    def play(self):
        if not self.player_hand:
            return ("Wygrał komputer")
        elif not self.computer_hand:
            return ("Wygrał gracz")

        player_card = self.player_hand.pop(0)
        computer_card = self.computer_hand.pop(0)
        self.table_cards.extend([player_card, computer_card])

        print(f'{player_card["rank"]} {player_card["suite"]} vs {computer_card["rank"]} {computer_card["suite"]}')

        if player_card['value'] > computer_card['value']:
            self.player_hand.append(player_card)
            self.player_hand.append(computer_card)
            return ("Wygrałeś")

        elif player_card['value'] < computer_card['value']:
            self.computer_hand.append(player_card)
            self.computer_hand.append(computer_card)
            return ("Wygrał Komputer")
        else:
            print("Wojna!")
            if len(self.player_hand) < 2 or len(self.computer_hand) < 2:
                return ("Nie można kontynuować wojny, któraś z rąk jest za krótka")
            self.table_cards.extend(
                [self.player_hand.pop(0), self.computer_hand.pop(0)])
            return self.play()


def print_hand(hand):
    for card in hand:
        print(f'{card["rank"]}  {card["suite"]}', end=', ')
    print()


def main():
    hand = Hand()
    player_hand, computer_hand = hand.deal_cards()
    game = Game(player_hand, computer_hand)

    while player_hand and computer_hand:
        result = game.play()
        print(result)
        if result and "Nie można" in result:
            break

        kontynuuj = input("Czy chcesz kontynuować grę? ENTER: ")
        if kontynuuj.lower() == 'koniec':
            break
        elif kontynuuj.lower() == 'dawaj':
            print("Ręka gracza:")
            print_hand(player_hand)
            print("Ręka komputera:")
            print_hand(computer_hand)

if __name__ == "__main__":
    main()