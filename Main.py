import player
class Game():
    def __init__(self) -> None:
        self.board = self.make_board()
        self.current_winner=None

    def make_board(self):
        return [" " for i in range(9)]

    def print_board(self):
        for i in range(0,7,3):
            print(self.board[i]+" | "+self.board[i+1]+" | "+self.board[i+2])

    def print_board_nums(self):
        #Ref board:
        # 0 | 1 | 2
        # 3 | 4 | 5
        # 6 | 7 | 8

        for i in range(0,7,3):
            print(str(i)+" | "+str(i+1)+" | "+str(i+2))

    def valid_moves(self):
        valid=[]
        for i in range(9):
            if self.board[i]==" ":
                valid.append(i)
        return valid
    
    
    def make_move(self, position, symbol):
        if position in self.valid_moves():
            self.board[position]=symbol
            if self.check_winner(symbol):
                self.current_winner=symbol
            return True
        return False
    
    def check_winner(self,symbol):
        #checking rows
        for i in range(0,7,3):
            if self.board[i]==self.board[i+1]==self.board[i+2]==symbol:
                return True
        
        #checking columns:
        for i in range(3):
            if self.board[i]==self.board[i+3]==self.board[i+6]==symbol:
                return True
        
        #check diagnols
        if self.board[0]==self.board[4]==self.board[8]==symbol or self.board[2]==self.board[4]==self.board[6]==symbol:
            return True
        
        return False
    def check_empty(self):
        for i in self.board:
            if i == " ":
                return True 
        return False
    def num_empty_squares(self):
        val=0
        for i in self.board:
            if i == " ":
                val+=1
        return val

def play_game(game, X_player, O_player, printing=True):

    if printing:
        game.print_board_nums()

    symbol="X"
    position=0
    while game.check_empty():
        if symbol=="O":
            position=O_player.get_move(game)
        else:
            position=X_player.get_move(game)
        
        if game.make_move(position,symbol):

            if printing:
                print("player "+symbol+": "+"makes move "+str(position)+" and we have new board:")
                game.print_board()
                print("")
            
            if game.current_winner:
                print("Player "+symbol+" Wins!!")
                break
            if not game.current_winner and game.num_empty_squares()==0:
                print("It's a Tie")
                break

            if symbol=="O":
                symbol="X"
            else:
                symbol="O"
        
if __name__ == "__main__":
    while True:
        game= Game()

        #getting types
        print("Welcome to Tic-Tac-Toe")
        print("")
        print("1:Human Player  2:Dumb-Computer  3:Smart-Computer")
        print("")
        t1=int(input("Enter X player type: "))
        t2=int(input("Enter O player type: "))
        while t1 not in [1,2,3] and t2 not in [1,2,3]:
            print("Invalid, try again")
            print("1:Human Player  2:Dumb-Computer  3:Smart-Computer")
            t1=int(input("Enter X player type: "))
            t2=int(input("Enter O player type: "))

        if t1==1:
            x_player = player.Human_Player("X")
        if t1==2:
            x_player= player.Random_Player("X")
        if t1==3:
            x_player= player.Smart_Player("X")

        if t2==1:
            o_player = player.Human_Player("O")
        if t2==2:
            o_player= player.Random_Player("O")
        if t2==3:
            o_player= player.Smart_Player("O")

        #Play:
        play_game(game,x_player,o_player)
    









