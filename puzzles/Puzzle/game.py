if __name__ == "__main__":
    from tiles import *
else:
    from puzzles.Puzzle.tiles import *
import time

def unique(lst: list):
    output = []
    for i in lst:
        if i not in output:
            output.append(i)

    return output

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

        self.location = (2, 2)


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
        self.setGravity(gravity)


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
        if isinstance(index, Fart) or isinstance(index, tuple) or isinstance(index, list):
            return self.tiles[index[1]][index[0]]
        else:
            return self.tiles[index]
    

class Puzzle:
    def __init__(self, boards, startTiles = [Start1]):
        self.boards = boards
        for board in boards:
            board.setPuzzle(self)
        self.farts = []
        self.startTiles = startTiles
        self.state = "initializing"
        self.waiting = False


    def __getitem__(self, index):
        if isinstance(index, Fart) or isinstance(index, tuple) or isinstance(index, list):
            return self.boards[index[2]][index]
        else:
            return self.boards[index]
        

    def __setitem__(self, index, tile):
        if isinstance(index, Fart):
            fart = index
            self[fart.z][fart.y][fart.x] = tile
        else:
            self[index[2]][index[1]][index[0]] = tile


    def __str__(self):
        return "\n\n\n".join([str(board) for board in self.boards])
    

    def unique(self, lst: list):
        output = []
        for i in lst:
            if i not in output:
                output.append(i)

        return output
    

    def isoob(self, fart):
        x, y, z = fart.coords() if isinstance(fart, Fart) else fart
        if z >= 0 and z < len(self.boards):
            board = self[z]
            if (x >= 0 and x < board.width and
                y >= 0 and y < board.height):
                    return False

        return True
    

    def filter(self, indeces):
        """returns a list of indeces that arent out of bounds"""
        filteredIndeces = []
        for index in indeces:
            x, y, z = index
            if z >= 0 and z < len(self.boards):
                board = self[z]
                if (x >= 0 and x < board.width and
                    y >= 0 and y < board.height):
                    filteredIndeces.append(index)

        return filteredIndeces


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
        # early activates
        for fart in self.farts:
            tile = fart.tile()
            tile.earlyactivate(fart)

        # print(self)

        for fart in self.farts:
            tile = fart.tile()

            # normal activate
            tile.activate(fart)
            disableaoe = tile.disableaoe

            # aoe effects
            fart.aoemovement = False
            if disableaoe is False:
                for aoetile in self.aoeTiles:
                    if aoetile in [self[index] for index in self.filter(aoetile.aoe(fart))]:
                        aoetile.trigger(fart)

            # next movement
            if fart.aoemovement is False:
                fart.moveto(tile.next(fart))


    def start(self):
        for startTile in self.startTiles:
            startIndeces = self.findTileIndeces(startTile)
            startIndex = int(input("Start at ")) - 1
            self.createFart(startIndeces[startIndex], startloc = startIndex + 1)

            self.aoeTiles = unique([tile for board in self.boards for y in board for tile in y if tile.aoe(self.farts[0]) is not None])


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
            return None
        elif self.state == "lose":
            print("lose :(")
            return None

        for fart in self.farts:
            if self.isoob(fart):
                raise IndexError('the fart has fallen out of the board i fear')