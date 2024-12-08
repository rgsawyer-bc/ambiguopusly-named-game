class Tile:
    def __init__(self, puzzle):
        self.puzzle = puzzle


    def __eq__(self, other):
        return self.shorthand == other.shorthand
    

    def balloon(self):
        return self.board.balloon


class Start(Tile):
    shorthand = "air"
    emojiname = ":one:"
    emoji = "1️⃣"
    description = "start here"


    def activate(self):
        self.board.fart.fall()


class Air(Tile):
    shorthand = "air"
    emojiname = ":black_large_square:"
    emoji = "⬛"
    description = "A blank tile. Fart passes through normally with no strings attached."


    def activate(self):
        self.puzzle.fart.fall()


class LeftRamp(Tile):
    shorthand = "air"
    emojiname = ":black_large_square:"
    emoji = "⬛"
    description = "push the the left lol"


    def activate(self):
        self.puzzle.fart.fall()
        self.puzzle.fart.left()


print(Air('h').shorthand)

# right ✒️ 💨 left🖋️