import imp
import math
import random

class Player():

    def __init__(self, symbol) -> None:
        self.symbol=symbol
        self.winner=None

    def get_move(self, game):
        pass
    
class Human_Player(Player):

    def __init__(self, symbol) -> None:
        super().__init__(symbol)

    def get_move(self, game):
        valid_position = False
        position = None

        while not valid_position:
            position = int(input("Player "+self.symbol+": "+"Enter your next move position: "))
            if position in game.valid_moves():
                valid_position=True
            else:
                print("Invalid, Try again")
        return position

class Random_Player(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
    def get_move(self, game):
        return random.choice(game.valid_moves())

class Smart_Player(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
    def get_move(self, game):
        if len(game.valid_moves()) == 9:
            square = random.choice(game.valid_moves())
        else:
            square = self.minimax(game, self.symbol)['position']
        return square

    def minimax(self, state, player):
        max_player = self.symbol 
        other_player = 'O' if player == 'X' else 'X'

        # check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.check_empty():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.valid_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
            
