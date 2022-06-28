
class AMorrisonPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_move(self, board=None, symbol=None):
        # Only ever chooses the same move, can't be used to play a complete game
        return [0, 0]
