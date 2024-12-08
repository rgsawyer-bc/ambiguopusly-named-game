from tiles import *

class Fart:
    def __init__(self, coords, puzzle, direction = 1):
        """direction is 1 or -1, 1 is for down"""
        self.coords = coords
        self.direction = direction
        self.puzzle = puzzle
        self.emoji = "w"
        
        self.x, self.y, self.z = coords


    def up(self):
        gravity = self.puzzle[self.z].gravity
        self.x += gravity[0]
        self.y += gravity[1]

    
    def down(self):
        self.coords[0] += 1


    def left(self):
        self.coords[1] -= 1


    def right(self):
        self.coords[1] += 1


    def move(self):
        self.coords[0] += self.direction


    def teleport(self, location):
        self.coords = location


    def __index__(self):
        return self.coords[1], self.coords[0]


class Board:
    def __init__(self, width, height, tiles):
        self.width = width
        self.height = height

        if len(tiles) != width * height:
            raise ValueError("dumbass")
        
        board = [[Air for x in range(width)] for y in range(height)]
        for x in range(width):
            for y in range(height):
                board[y][x] = tiles[(width)*y + x](self)

        self.tiles = board

        self.gravity = [0, 1] # oh boy this shits gonna get weird
            # instead of making each thing refer explicitly to a relative index, make a function that returns the "left direction" (or other directions) given a gravity


    def setGravity(self, gravity):
        """gravity is down, up, left, or right"""
        if gravity == "down":
            self.gravity = [0, 1]
        elif gravity == "up":
            self.gravity = [0, -1]
        elif gravity == "right":
            self.gravity = [1, 0]
        else:
            self.gravity == [-1, 0]


    def __str__(self):
        rawtiles = "\n".join([
            " ".join([tile.emoji for tile in j])
        for j in self.tiles])

        return rawtiles
    

    def __getitem__(self, index):
        if isinstance(index, Fart):
            return self.tiles[index[1]][index[0]]
        else:
            return self.tiles[index]
    

class Puzzle:
    def __init__(self, boards):
        self.boards = boards
        self.fart = Fart([0, 0, 0], self)


    def __getitem__(self, index):
        return self.boards[index]


    def findTiles(self, tile):
        foundIndeces = []
        for z, board in enumerate(self.boards):
            for y in range(board.height):
                for x in range(board.width):
                    currentTile = board[y][x]
                    if currentTile == tile:
                        foundIndeces.append([x, y, z])
                    




b = [Air for i in range(30)]

bongo = Board(5, 6, b)

print(bongo)

