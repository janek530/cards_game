class Card:


    def __init__(self, card, color, id):
        self.card = card
        self.color = color
        self.id = id

    def __str__(self):
        return self.id

    def get_card_info(self):
        return 'card: {} color: {}'.format(self.card, self.color)


