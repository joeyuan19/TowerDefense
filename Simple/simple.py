
PATH  = 0 
WALL  = 1
TOWER = 2
CREEP = 3

SYMBOLS = {
    PATH  : '.',
    WALL  : '#',
    TOWER : '^',
    CREEP : 'c'
}

class Board(object):
    def __init__(self,length=1,width=1):
        self.length = length
        self.width = width
        self.board = [[0 for i in range(length)] for j in range(width)]
   
    def load(self,board):
        self.length = len(board[0])
        self.width  = len(board[0])
        self.board  = board

    def print_board(self):
        print('\n'.join(''.join(SYMBOLS[i] for i in row) for row in self.board) + '\n')

class GamePiece(object):
    def __init__(self,position):
        self.position = position

    def set_position(self,position):
        self.position

    def set_x(self,x):
        self.position[0] = x

    def set_y(self,y):
        self.position[1] = y

class Creep(GamePiece):
    def __init__(self,speed,hp,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        self.speed = speed
        self.hp = hp
    
class Tower(GamePiece):
    def __init__(self,position,power):
        self.position = position
        self.power = power
        
class TowerDefense(object):
    def __init__(self):
        self.board = Board()

    def load(self,board):
        self.board = board

    def start(self):
        pass
                


t = TowerDefense()
t.load([[1 1 1],
        [0 0 0],
        [1 1 1]])





