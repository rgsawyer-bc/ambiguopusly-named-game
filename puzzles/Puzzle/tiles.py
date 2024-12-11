import random

class Tile:
    def __init__(self, puzzle = None):
        self.puzzle = puzzle
        self.disableaoe = False
        self.active = False


    def __eq__(self, other):
        return self.shorthand == other.shorthand
    

    def balloon(self):
        return self.board.balloon
    

    def next(self, fart):
        return fart.down()
    

    def activate(self, fart):
        pass


    def earlyactivate(self, fart):
        pass


    def aoe(self, fart):
        return None
    

class Start1(Tile):
    shorthand = "start1"
    emojiname = ":one:"
    emoji = "1️⃣ "
    description = "start here"
    location = (1, 0)


class Start2(Tile):
    shorthand = "start2"
    emojiname = ":two:"
    emoji = "2️⃣ "
    description = "start here"
    location = (2, 0)


class Start3(Tile):
    shorthand = "start3"
    emojiname = ":three:"
    emoji = "3️⃣ "
    description = "start here"
    location = (3, 0)


class Air(Tile):
    shorthand = "air"
    emojiname = ":black_large_square:"
    emoji = "⬛"
    description = "A blank tile. Fart passes through normally with no strings attached."
    location = (0, 0)


class RightRamp(Tile):
    shorthand = "rightramp"
    emojiname = ":black_large_square:"
    emoji = "↘️ "
    description = "push the the right lol"
    location = (10, 0)


    def next(self, fart):
        if fart.board.gravity[0] == 0:
            left = fart.left()
            down = fart.down()
            return [left[0], down[1], fart.z]
        elif fart.board.gravity[0] in [-1, 1]:
            right = fart.right()
            down = fart.down()
            return [down[0], right[1], fart.z]
        else:
            return ValueError("invalid gravity (how?)")


class LeftRamp(Tile):
    shorthand = "leftramp"
    emojiname = ":black_large_square:"
    emoji = "🖋️ "
    description = "push the the left lol"
    location = (11, 0)


    def next(self, fart):
        if fart.board.gravity[0] == 0:
            right = fart.right()
            down = fart.down()
            return [right[0], down[1], fart.z]
        elif fart.board.gravity[0] in [-1, 1]:
            left = fart.left()
            down = fart.down()
            return [down[0], left[1], fart.z]
        else:
            return ValueError("invalid gravity (how?)")
        

class GravityDown(Tile):
    shorthand = "gravitydown"
    emojiname = ":black_large_square:"
    emoji = "⬇️ "
    description = "switches board gravity to down"
    location = (12, 0)


    def activate(self, fart):
        board = fart.z
        self.puzzle[board].setGravity("down")


class GravityLeft(Tile):
    shorthand = "gravityleft"
    emojiname = ":black_large_square:"
    emoji = "⬅️ "
    description = "switches board gravity to left"
    location = (13, 0)


    def activate(self, fart):
        board = fart.z
        self.puzzle[board].setGravity("left")


class GravityRight(Tile):
    shorthand = "gravityright"
    emojiname = ":black_large_square:"
    emoji = "➡️ "
    description = "switches board gravity to right"
    location = (14, 0)


    def activate(self, fart):
        board = fart.z
        self.puzzle[board].setGravity("right")


class GravityUp(Tile):
    shorthand = "gravityup"
    emojiname = ":black_large_square:"
    emoji = "⬆️ "
    description = "switches board gravity to up"
    location = (15, 0)


    def activate(self, fart):
        board = fart.z
        self.puzzle[board].setGravity("up")


class Bomb(Tile):
    shorthand = "bomb"
    emojiname = ":bomb:"
    emoji = "💣"
    description = "teleport to explosion"
    location = (0, 1)


    def next(self, fart):
        return fart.coords()


    def activate(self, fart):
        puzzle = fart.puzzle
        location = puzzle.findTileIndeces(Explosion)[0]
        fart.moveto(location)
        

class Explosion(Tile):
    shorthand = "boom"
    emojiname = ":boom:"
    emoji = "💥"
    description = "bomb explodes here"
    location = (1, 1)


class Helicopter(Tile):
    shorthand = "helicopter"
    emojiname = ":helicopter:"
    emoji = "🚁"
    description = "go back up"
    location = (2, 1)


    def next(self, fart):
        return [fart.x, 0, fart.z]
    

    def activate(self, fart):
        fart.puzzle[fart] = Air(fart.puzzle)
        

class FigglesEntrance(Tile):
    shorthand = "figglesentrance"
    emojiname = ":clown:"
    emoji = "🤡"
    description = "go to figgles land"
    location = (3, 1)


    def next(self, fart):
        return fart.coords()


    def activate(self, fart):
        puzzle = fart.puzzle
        location = puzzle.findTileIndeces(FigglesExit)[0]
        fart.moveto(location)


class FigglesExit(Tile):
    shorthand = "figglesexit"
    emojiname = ":clown:"
    emoji = "🤡"
    description = "you are now in figgles land"
    location = (3, 1)


class CircusEntrance(Tile):
    shorthand = "circusentrance"
    emojiname = ":circus_tent:"
    emoji = "🎪"
    description = "leave figgles land"
    location = (4, 1)


    def next(self, fart):
        return fart.coords()


    def activate(self, fart):
        puzzle = fart.puzzle
        location = puzzle.findTileIndeces(CircusExit)[0]
        fart.moveto(location)


class CircusExit(Tile):
    shorthand = "circusexit"
    emojiname = ":circus_tent:"
    emoji = "🎪"
    description = "you have left figgles land"
    location = (4, 1)


class Hole(Tile):
    shorthand = "hole"
    emojiname = ":hole:"
    emoji = "🕳️ "
    description = "die"
    location = (5, 1)


    def next(self, fart):
        return fart.coords()
    

    def activate(self, fart):
        fart.puzzle.state = "lose"


class Grandma(Tile):
    shorthand = "grandma"
    emojiname = ":older_woman:"
    emoji = "👵"
    description = "win"
    location = (6, 1)


    def next(self, fart):
        return fart.coords()
    

    def activate(self, fart):
        fart.puzzle.state = "win"


class Dice(Tile):
    shorthand = "dice"
    emojiname = ":game_die:"
    emoji = "🎲"
    description = "randomly go left or right"
    location = (7, 1)


    def next(self, fart):
        choices = [fart.left(), fart.right()]
        return random.choice(choices)


class Balloon(Tile):
    shorthand = "balloon"
    emojiname = ":balloon:"
    emoji = "🎈"
    description = "up"
    location = (8, 1)


    def earlyactivate(self, fart):
        fart.emoji = "🎈"
        fart.location = (8, 1)


    def activate(self, fart):
        fart.direction = -1
        fart.puzzle[fart] = Air(fart.puzzle)


class Cactus(Tile):
    shorthand = "cactus"
    emojiname = ":cactus:"
    emoji = "🌵"
    description = "cactus"
    location = (9, 1)

    
    def earlyactivate(self, fart):
        fart.emoji = "💨"
        fart.location = (2, 2)


    def activate(self, fart):
        fart.direction = 1
        

class Sparkle(Tile):
    shorthand = "sparkle"
    emojiname = ":sparkles:"
    emoji = "✨"
    description = "sparkle"
    location = (10, 1)


class Wizard(Tile):
    shorthand = "wizard"
    emojiname = ":man_mage:"
    emoji = "🧙"
    description = "wizard"
    location = (11, 1)


    def earlyactivate(self, fart):
        sparkleIndex1, sparkleIndex2 = fart.puzzle.findTileIndeces(Sparkle)
        x1, y1, z1 = sparkleIndex1
        tile1Index = (x1, y1 + 1, z1)
        x2, y2, z2 = sparkleIndex2
        tile2Index = (x2, y2 + 1, z2)
        
        tile1 = fart.puzzle[tile1Index]
        tile2 = fart.puzzle[tile2Index]

        fart.puzzle[tile1Index] = tile2
        fart.puzzle[tile2Index] = tile1


class Scale(Tile):
    shorthand = "scale"
    emojiname = ":scales:"
    emoji = "⚖️ "
    description = "scale"
    location = (12, 1)


    def next(self, fart):
        if fart.startloc % 2 == 0:
            return RightRamp(fart.puzzle).next(fart)
        else:
            return LeftRamp(fart.puzzle).next(fart)


class Lightning(Tile):
    shorthand = "lightning"
    emojiname = ":zap:"
    emoji = "⚡"
    description = "lightning"
    location = (13, 1)


    def aoe(self, fart):
        return [fart.left(), fart.right()]
    

    def trigger(self, fart):
        puzzle = fart.puzzle
        if fart.direction == -1:
            fart.aoemovement = True
            if isinstance(puzzle[fart.left()], Lightning) and puzzle.isoob(fart.left()) is False:
                fart.moveto(fart.left())
            else:
                fart.moveto(fart.right())


class Door(Tile):
    shorthand = "door"
    emojiname = ":door:"
    emoji = "🚪"
    description = "door"
    location = (14, 1)


    def activate(self, fart):
        fart.puzzle.state = "lose"


class Key(Tile):
    shorthand = "key"
    emojiname = ":key:"
    emoji = "🔑"
    description = "key"
    location = (15, 1)


    def earlyactivate(self, fart):
        puzzle = fart.puzzle
        puzzle[puzzle.findTileIndeces(Door)[0]] = Air(fart.puzzle)
        puzzle[fart] = Air()


class Basket(Tile):
    shorthand = "basket"
    emojiname = ":wastebasket:"
    emoji = "🗑️ "
    description = "basket"
    location = (1, 2)


class Basketball(Tile):
    shorthand = "basketball"
    emojiname = ":basketball:"
    emoji = "🏀"
    description = "basketball"
    location = (0, 2)


    def activate(self, fart):
        self.disableaoe = True
        basketIndeces = self.puzzle.findTileIndeces(Basket)

        chosenBasket = None
        while chosenBasket not in basketIndeces:
            chosenBasket = fart.puzzle.pygame.input()

        fart.moveto(chosenBasket)


    def next(self, fart):
        return fart.coords()

    



# tile which you choose what direction ramp it is in the beginning
# tile that lets you put thing at top again
# tile that shifts row to left/right/lets you choose
# tile where you choose what direction ramp it is when you land on it
# tiles that when you land on them, you get the ability to do something later on
# tile that pulls farts towards it (?)

# this code is designed to handle multiple farts on multiple boards at the same time:
    # tile that splits a fart into two farts
    # tile that lets you place a new fart
    # local gravity switch, global gravity switch (gravity switches only change the gravity for the current board, another tile could change gravity for every board)
    # perhaps require that each fart land on a grandma
