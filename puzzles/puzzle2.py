from puzzles.Puzzle.game import *

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