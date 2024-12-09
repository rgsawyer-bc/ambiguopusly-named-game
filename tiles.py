from random import random

class Tile:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.disableAOE = False


    def __eq__(self, other):
        return self.shorthand == other.shorthand
    

    def balloon(self):
        return self.board.balloon
    

    def next(self, fart):
        return fart.down()
    

    def activate(self, fart):
        pass


    def aoe(self, fart):
        return None
    

class Start1(Tile):
    shorthand = "start1"
    emojiname = ":one:"
    emoji = "1️⃣ "
    description = "start here"


class Start2(Tile):
    shorthand = "start2"
    emojiname = ":two:"
    emoji = "2️⃣ "
    description = "start here"


class Air(Tile):
    shorthand = "air"
    emojiname = ":black_large_square:"
    emoji = "⬛"
    description = "A blank tile. Fart passes through normally with no strings attached."


class RightRamp(Tile):
    shorthand = "rightramp"
    emojiname = ":black_large_square:"
    emoji = "↘️ "
    description = "push the the right lol"


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


    def activate(self, fart):
        board = fart.z
        self.puzzle[board].setGravity("down")


class GravityLeft(Tile):
    shorthand = "gravityleft"
    emojiname = ":black_large_square:"
    emoji = "⬅️ "
    description = "switches board gravity to left"


    def activate(self, fart):
        board = fart.z
        self.puzzle[board].setGravity("left")


class GravityRight(Tile):
    shorthand = "gravityright"
    emojiname = ":black_large_square:"
    emoji = "➡️ "
    description = "switches board gravity to right"


    def activate(self, fart):
        board = fart.z
        self.puzzle[board].setGravity("right")


class GravityUp(Tile):
    shorthand = "gravityup"
    emojiname = ":black_large_square:"
    emoji = "⬆️ "
    description = "switches board gravity to up"


    def activate(self, fart):
        board = fart.z
        self.puzzle[board].setGravity("up")


class Bomb(Tile):
    shorthand = "bomb"
    emojiname = ":bomb:"
    emoji = "💣"
    description = "teleport to explosion"


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


class Helicopter(Tile):
    shorthand = "helicopter"
    emojiname = ":helicopter:"
    emoji = "🚁"
    description = "go back up"


    def next(self, fart):
        return [fart.x, 0, fart.z]
    

    def activate(self, fart):
        fart.puzzle[fart] = Air(fart.puzzle)
        

class FigglesEntrance(Tile):
    shorthand = "figglesentrance"
    emojiname = ":clown:"
    emoji = "🤡"
    description = "go to figgles land"


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


class CircusEntrance(Tile):
    shorthand = "circusentrance"
    emojiname = ":circus_tent:"
    emoji = "🎪"
    description = "leave figgles land"


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


class Hole(Tile):
    shorthand = "hole"
    emojiname = ":hole:"
    emoji = "🕳️ "
    description = "die"


    def next(self, fart):
        return fart.coords()
    

    def activate(self, fart):
        fart.puzzle.state = "lose"


class Grandma(Tile):
    shorthand = "hole"
    emojiname = ":older_woman:"
    emoji = "👵"
    description = "win"


    def next(self, fart):
        return fart.coords()
    

    def activate(self, fart):
        fart.puzzle.state = "win"


class Dice(Tile):
    shorthand = "hole"
    emojiname = ":older_woman:"
    emoji = "🎲"
    description = "win"


    def next(self, fart):
        choices = [fart.left(), fart.right()]
        return random.choice(choices)






# right ✒️ 💨 left🖋️


# tile which you choose what direction ramp it is in the beginning
# multiple boards, multiple fart starting locations
# local gravity switch, global gravity switch