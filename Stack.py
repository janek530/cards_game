from Card import Card
import numpy as np
class Stack:

    def __init__(self, talia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A'], colors = ['H', 'P', 'R', 'K']):
        self.cards = []
        self.talia = talia
        self.colors = colors
        self.id = len(self.talia)*len(self.colors)
        id = 1
        for card in self.talia:
            for color in self.colors:
                self.cards.append(Card(card, color, id))
                id += 1

        print(self.shuffle_stack())

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):

        return self.cards[item]

    def shuffle_stack(self):
        array_cards = np.array(self.cards)
        return array_cards

    def get_cards(self):
        return self.cards