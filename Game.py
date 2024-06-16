class Game:

    players = []

    def __init__(self, players: int, ):
        self.create_board()

    def create_board(self, players: int):
        self.players = players