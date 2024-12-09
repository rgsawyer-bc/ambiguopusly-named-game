from tiles import *
import time

class Fart:
    def __init__(self, coords, puzzle, startloc, direction = 1, start = 1):
        """direction is 1 or -1, 1 is for down"""
        self.direction = direction
        self.puzzle = puzzle
        self.emoji = "💨"
        self.start = start
        self.startloc = startloc
        
        self.x, self.y, self.z = coords

        self.board = puzzle.boards[self.z]


    def getGravity(self):
        gravity = self.puzzle[self.z].gravity[:]
        gravity[0] *= self.direction
        gravity[1] *= self.direction

        return gravity


    def up(self):
        gravity = self.getGravity()
        x = self.x - gravity[0]
        y = self.y - gravity[1]
        return [x, y, self.z]

    
    def down(self):
        gravity = self.getGravity()
        x = self.x + gravity[0]
        y = self.y + gravity[1]
        return [x, y, self.z]


    def right(self):
        gravity = self.getGravity()
        if gravity[0] == 0:
            x = self.x - gravity[1]
            return [x, self.y, self.z]
        else:
            y = self.y + gravity[0]
            return [self.x, y, self.z]


    def left(self):
        gravity = self.getGravity()
        if gravity[0] == 0:
            x = self.x + gravity[1]
            return [x, self.y, self.z]
        else:
            y = self.y - gravity[0]
            return [self.x, y, self.z]


    def moveto(self, location):
        self.x, self.y, self.z = location


    def coords(self):
        return [self.x, self.y, self.z]
    

    def tile(self):
        return self.puzzle[self]


    def __index__(self):
        return tuple(self.coords())
    

    def __getitem__(self, index):
        return [self.x, self.y, self.z][index]
    

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


class Board:
    def __init__(self, width, height, tiles, gravity = "down"):
        self.width = width
        self.height = height

        if len(tiles) != width * height:
            raise ValueError("dumbass")

        self.tiles = tiles
        self.setGravity(gravity) # oh boy this shits gonna get weird
            # instead of making each thing refer explicitly to a relative index, make a function that returns the "left direction" (or other directions) given a gravity


    def setPuzzle(self, puzzle):
        self.puzzle = puzzle
        width, height = self.width, self.height
        board = [[Air for x in range(width)] for y in range(height)]
        for x in range(width):
            for y in range(height):
                board[y][x] = self.tiles[(width)*y + x](puzzle)

        self.tiles = board


    def setGravity(self, gravity):
        """gravity is down, up, left, or right"""
        if gravity == "down":
            self.gravity = [0, 1]
        elif gravity == "up":
            self.gravity = [0, -1]
        elif gravity == "right":
            self.gravity = [1, 0]
        elif gravity == "left":
            self.gravity = [-1, 0]
        else:
            raise ValueError('BUNGLE')


    def __str__(self):
        boardIndex = self.puzzle.boards.index(self)
        tileEmojis = [[tile.emoji for tile in j] for j in self.tiles]
        for fart in self.puzzle.farts:
            if fart.z == boardIndex:
                tileEmojis[fart.y][fart.x] = fart.emoji
        rawtiles = "\n".join([
            " ".join(j)
        for j in tileEmojis])

        return rawtiles
    

    def __getitem__(self, index):
        if isinstance(index, Fart) or isinstance(index, tuple):
            return self.tiles[index[1]][index[0]]
        else:
            return self.tiles[index]
        

    # define in boolean to check if fart in board
    

class Puzzle:
    def __init__(self, boards, startTiles = [Start1]):
        self.boards = boards
        for board in boards:
            board.setPuzzle(self)
        self.farts = []
        self.startTiles = startTiles
        self.state = "initializing"


    def __getitem__(self, index):
        if isinstance(index, Fart) or isinstance(index, tuple):
            return self.boards[index[2]][index]
        else:
            return self.boards[index]
        

    def __setitem__(self, index, tile):
        if isinstance(index, Fart):
            fart = index
            self[fart.z][fart.y][fart.x] = tile
        elif isinstance(index, tuple):
            self[index[2]][index[1]][index[0]] = tile


    def __str__(self):
        return "\n\n\n".join([str(board) for board in self.boards])


    def createFart(self, coords, startloc):
        self.farts.append(Fart(coords, self, startloc))


    def findTileIndeces(self, tile):
        foundIndeces = []
        for z, board in enumerate(self.boards):
            for y in range(board.height):
                for x in range(board.width):
                    currentTile = board[y][x]
                    if currentTile == tile:
                        foundIndeces.append([x, y, z])

        return foundIndeces

    
    def update(self):
        for fart in self.farts:
            tile = fart.tile()
            tile.earlyactivate(fart)

        print(self)

        for fart in self.farts:
            tile = fart.tile()
            tile.activate(fart)
            fart.moveto(tile.next(fart))


    def start(self):
        for startTile in self.startTiles:
            startIndeces = self.findTileIndeces(startTile)
            startIndex = int(input("Start at ")) - 1
            self.createFart(startIndeces[startIndex], startloc = startIndex + 1)


    def play(self):
        self.state = "playing"
        print(self)
        self.start()
        while self.state == "playing":
            print("\n -=============================================================================================- \n")
            time.sleep(.5)
            self.update()

        if self.state == "win":
            print("win :D")
        else:
            print("lose :(")
                    

mainBoard = [
    Start1, Start1, Start1, Start1, Start1, Start1, Start1, 
    Air, Air, Cactus, Air, Cactus, Air, LeftRamp,
    Air, Air, Air, Air, Air, Air, Air, 
    Air, Air, Bomb, Air, Air, Scale, Air, 
    RightRamp, Air, Air, Air, Air, RightRamp, Air, 
    Air, Wizard, Air, RightRamp, Air, Air, Air, 
    Sparkle, Air, Air, Air, Air, Air, Sparkle,
    Helicopter, Air, LeftRamp, Air, Scale, Air, CircusExit,
    Air, RightRamp, Air, Air, LeftRamp, Air, Air, 
    Air, Air, Air, Air, Explosion, Air, Air, 
    Air, Air, Air, Air, Air, LeftRamp, Air, 
    RightRamp, Air, Balloon, FigglesEntrance, Air, Air, Air, 
    Hole, Grandma, Hole, Hole, Hole, Hole, Hole
]

figglesBoard = [
    Air, FigglesExit, Air, 
    Air, Air, Air, 
    Air, Scale, Air, 
    Air, Air, Air, 
    Air, Air, Air, 
    Air, Air, Air, 
    CircusEntrance, Hole, Hole
]
mainBoard = Board(7, 13, mainBoard)
figglesBoard = Board(3, 7, figglesBoard)
Puzzle2 = Puzzle([mainBoard, figglesBoard], startTiles = [Start1])

Puzzle2.play()