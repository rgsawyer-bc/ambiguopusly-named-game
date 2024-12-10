import sys
sys.path.insert(1, r"C:\Users\Graham\Documents\ambiguopusly-named-game\Puzzle")
from game import *

mainBoard = [
    Start1, Start1, Start1, Start1, Start1, Start1, Start1, 
    Air, Air, Air, Air, Air, Air, Air,
    Explosion, Air, Air, Air, Air, Hole, Air,
    Air, Air, Air, Air, RightRamp, Air, Air,
    Air, LeftRamp, Air, Air, Air, Air, Air,
    Air, Air, Air, LeftRamp, Air, Air, Bomb,
    Air, Air, LeftRamp, CircusExit, Air, Air, Air,
    Air, Air, Air, Air, Air, Air, Air,
    RightRamp, Air, Air, LeftRamp, Air, FigglesEntrance, Air,
    Air, Air, Air, Air, Air, Air, RightRamp,
    Air, Air, RightRamp, Air, LeftRamp, Air, Air,
    Air, Helicopter, Air, Air, Air, Air, Air, 
    Hole, Hole, Hole, Grandma, Hole, Hole, Hole
]
figglesBoard = [
    Air, FigglesExit, Air,
    Air, Air, Air,
    Air, Dice, Air,
    Air, Air, Air, 
    Air, Air, Air, 
    Air, Air, Air, 
    Hole, Hole, CircusEntrance
]
mainBoard = Board(7, 13, mainBoard)
figglesBoard = Board(3, 7, figglesBoard)
Puzzle1 = Puzzle([mainBoard, figglesBoard], startTiles = [Start1])