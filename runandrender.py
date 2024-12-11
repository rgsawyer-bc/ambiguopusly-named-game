import pygame
from puzzles.puzzle3 import Puzzle3
from puzzles.puzzle2 import Puzzle2
import time

class PuzzleGame:
    def __init__(self, puzzle):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 100)
        self.window = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Discover Python & Patterns")
        self.clock = pygame.time.Clock()
        self.running = True
        self.puzzle = puzzle
        self.texture = pygame.image.load("tileset.png")

        innerbuffer = 64*3
        lowerfromtop = 100

        totalTileWidth = 64 * sum(board.width for board in puzzle.boards) + innerbuffer
        tileHeights = [64 * board.height - lowerfromtop for board in puzzle.boards]

        xstart = (1920 - totalTileWidth)/2
        # ystart = (1080 - totalTileHeight)/2

        self.xstarts = [xstart, xstart + 64*puzzle.boards[0].width + innerbuffer]
        self.ystarts = [(1080 - height)/2 for height in tileHeights]

        puzzle.pygame = self


    def clickToIndex(self, pos):
        mousex, mousey = pos
        for z, board in enumerate(self.puzzle.boards):
            for y in range(board.height):
                for x in range(board.width):
                    tilex, tiley = self.tileLocations[z][y][x]
                    if mousex >= tilex and mousex < tilex + 64 and mousey >= tiley and mousey < tiley + 64:
                        return [x, y, z]
                    
        return None
        

    def click(self):
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                self.running = False

                raise Exception('bye guys')
                break

            if event.type == pygame.MOUSEBUTTONUP:
                return self.clickToIndex(pygame.mouse.get_pos())
            
        return None


    def input(self):
        index = None
        while index is None:
            index = self.click()

        return index
    

    def start(self):
        puzzle = self.puzzle
        puzzle.state = "playing"
        for startTile in puzzle.startTiles:
            startIndeces = puzzle.findTileIndeces(startTile)
            tile = None

            while not isinstance(tile, startTile):
                startIndex = self.input()
                tile = self.puzzle[startIndex]

            puzzle.createFart(startIndex, startIndeces.index(startIndex) + 1)

            puzzle.aoeTiles = puzzle.unique([tile for board in puzzle.boards for y in board for tile in y if tile.aoe(puzzle.farts[0]) is not None])


    def render(self):
        self.tileLocations = [[[(0, 0) for x in range(board.width)] for y in range(board.height)] for board in self.puzzle.boards]

        self.window.fill((0, 0, 0))


        for z, board in enumerate(self.puzzle.boards):
            xstart = self.xstarts[z]
            ystart = self.ystarts[z]

            for y, row in enumerate(board):
                for x, tile in enumerate(row):
                    tilesetx = 64 * tile.location[0]
                    tilesety = 64 * tile.location[1]
                    boardlocation = (xstart + 64*x, ystart + 64*y)

                    self.tileLocations[z][y][x] = boardlocation

                    farts = self.puzzle.farts
                    fartcoords = [fart.coords() for fart in farts]
                    self.window.blit(self.texture, boardlocation, pygame.Rect(tilesetx, tilesety, 64, 64))
                    if [x, y, z] in fartcoords:
                        # make this render the correct tile
                        self.window.blit(self.texture, boardlocation, pygame.Rect(128, 128, 64, 64))

        pygame.display.update()


    def checkEnd(self):
        if self.puzzle.state == "lose":
            text_surface = self.font.render('YOU FUCKING DIED', False, (255, 255, 255))
            self.window.blit(text_surface, (512, 512))
            pygame.display.update()
            

        if self.puzzle.state == "win":
            text_surface = self.font.render('win :D', False, (255, 255, 255))
            self.window.blit(text_surface, (512, 512))
            pygame.display.update()


    def run(self):
        self.render()
        self.start()
        self.render()

        while self.running:
            time.sleep(.25)
            self.click()

            if self.puzzle.state == "playing":
                self.puzzle.update()
                self.render()

                self.checkEnd()

game = PuzzleGame(Puzzle3)
game.run()

#pygame.init()
#window = pygame.display.set_mode((1920, 1080))

#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#            break

#    pygame.draw.rect(window,(0,0,255),(120,120,400,240))
#    pygame.display.update()    

#pygame.quit()