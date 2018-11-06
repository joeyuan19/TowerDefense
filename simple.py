DIM = (8,8)

class Tower(object):
    def __init__(self,x,y,char,radius):
        self.pos = (x,y)
        self.char = char
        self.bullets = []
        self.radius = radius

    def in_range(self,monster,road):
        mx,my = road.get_xy(monster.pos)
        tx,ty = self.pos
        if dist_2D(tx,ty,mx,my) <= r:
            return True
        else:
            return False

class Monster(object):
    def __init__(self,road_position,char,speed):
        self.pos = road_position
        self.char = char
        self.speed = speed
    
    def update(self):
        self.pos += self.speed

class Road(object):
    def __init__(self,path,char):
        self.path = path 
        self.char = char

    def get_xy(self,pos):
        if 0 <= pos < len(self.path):
            return self.path[pos]
        else:
            return None,None

def dist_2D(x1,y1,x2,y2):
    return abs(x2-x1) + abs(y2-y1)

def draw_board(towers,monsters,road):
    board = [[' ' for i in range(DIM[0])] for j in range(DIM[1])]
    for p in road.path:
        board[p[1]][p[0]] = road.char
    for t in towers:
        x,y = t.pos
        board[y][x] = t.char
        for b in t.bullets:
            board[y][x] = t.char
    for m in monsters:
        x,y = road.get_xy(m.pos)
        if x is not None:
            board[y][x] = m.char
    return '\n'.join(''.join(i) for i in board)

towers = [
    Tower(4,3,'t',2),
    Tower(5,3,'t',2),
    Tower(6,3,'t',2),
    Tower(7,3,'t',2),
]

monsters = [
    Monster(-5,'m',1),
]

road = Road([(i,4) for i in range(DIM[0])],'.')
print(road.path)

for i in range(20):
    print(board(towers,monsters,road))
    for m in monsters:
        m.update()
