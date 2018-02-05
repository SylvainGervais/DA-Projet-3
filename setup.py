#legend
WALL = "|M|"
ITEM = "<->"
FREE_SPACE = "   "
MAC_GYVER = "McG"
GUARDIAN = "!G!"
ON_ITEM = "<c>"
WITH_GUARDIAN = "!c!"
NB_ITEM = 3

#commands
MOVE_FRONT = "z"
MOVE_BACK = "s"
MOVE_LEFT = "q"
MOVE_RIGHT = "d"
PICKUP = " "
QUIT = "x"
PRINT = "c"


def printCommands():
    print("Commands for move Mac Gyver :")
    print("front :", MOVE_FRONT)
    print("back :", MOVE_BACK)
    print("left :", MOVE_LEFT)
    print("right :", MOVE_RIGHT)
    print("For pickup item hit space")
    print("For quit the game hit", QUIT)
    print()

