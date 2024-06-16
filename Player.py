from Stack import Stack

class Player:

    def __init__(self):
        for i in range(5):
            self.cards.append(self.get_card())

    def get_card(self, stack: Stack):
        pass

    def throw_card(self, card):
        pass

    def add_card(self, card: Card) -> list:
        self.__cards.append(card)

    def get_cards(self):
        return self.__cards