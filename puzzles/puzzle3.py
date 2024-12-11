from puzzles.Puzzle.game import *

mainBoard = [
    Start1, Start1, Start1, Start1, Start1, Start1, Start1, 
    Air, Air, Air, Air, Cactus, Air, Air, 
    Air, Air, Air, LeftRamp, Air, Air, Air, 
    Bomb, Key, Air, Air, Lightning, Basket, Air, 
    Cactus, Air, Air, Air, Air, Lightning, Air, 
    Sparkle, Air, Scale, Air, Air, Air, Air,
    Air, Air, Air, Air, Wizard, Explosion, Air, 
    Air, Air, Air, GravityRight, Air, RightRamp, Air, 
    Air, Basketball, Air, Air, Air, Air, Balloon,
    Sparkle, Air, Air, Air, Air, Air, Air,
    GravityDown, Air, Air, Air, Basket, Air, Air, 
    Door, LeftRamp, LeftRamp, Air, GravityLeft, Air, Air, 
    Grandma, Hole, Hole, Hole, Hole, Hole, Hole
]

mainBoard = Board(7, 13, mainBoard)
Puzzle3 = Puzzle([mainBoard], startTiles = [Start1])