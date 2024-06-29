import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    suits = ["hearts", "diamonds", "clubs", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

    def __init__(self, num_decks=1):
        self.cards = [Card(suit, value) for suit in Deck.suits for value in Deck.values] * num_decks
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        dealt_cards = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt_cards

class Player:
    def __init__(self, name, chip_balance=100):
        self.name = name
        self.hand = []
        self.chip_balance = chip_balance

    def draw_card(self, deck):
        self.hand.append(deck.deal(1)[0])

    def get_hand_value(self):
        value = 0
        aces = 0
        for card in self.hand:
            if card.value in ["jack", "queen", "king"]:
                value += 10
            elif card.value == "ace":
                aces += 1
                value += 11
            else:
                value += int(card.value)

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def place_bet(self, amount):
        if amount > self.chip_balance:
            raise ValueError("Insufficient chips")
        self.chip_balance -= amount
        return amount

    def __str__(self):
        return f"{self.name} with hand: {', '.join(str(card) for card in self.hand)}"

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def should_hit(self):
        return self.get_hand_value() < 17
    
class Game:
    def __init__(self, num_decks=1):
        self.deck = Deck(num_decks)

    def deal_initial_cards(self, player, dealer):
        player.hand = self.deck.deal(2)
        dealer.hand = self.deck.deal(1)

    def player_turn(self, player):
        while True:
            print(f"{player.name}'s hand: {', '.join(str(card) for card in player.hand)} (value: {player.get_hand_value()})")
            if player.get_hand_value() > 21:
                print(f"{player.name} busts!")
                break
            choice = input("Do you want to hit or stand? (h/s): ").lower()
            if choice == 'h':
                player.draw_card(self.deck)
            else:
                break

    def dealer_turn(self, dealer):
        while dealer.should_hit():
            dealer.draw_card(self.deck)
        print(f"Dealer's hand: {', '.join(str(card) for card in dealer.hand)} (value: {dealer.get_hand_value()})")

    def check_winner(self, player, dealer):
        player_value = player.get_hand_value()
        dealer_value = dealer.get_hand_value()
        if player_value > 21:
            return "Dealer wins"
        elif dealer_value > 21 or player_value > dealer_value:
            return f"{player.name} wins"
        elif player_value < dealer_value:
            return "Dealer wins"
        else:
            return "It's a tie"



