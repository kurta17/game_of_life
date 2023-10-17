import time
import turtle
import random

# Initialize the Turtle screen and Turtle object
wn = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.speed(0)
t.ht()

# Input for the grid size and delay between generations
length = int(input("How many cells across is the grid?"))
speed = float(input("How long is the delay between generations (seconds)"))

# Create a random grid of cells
CellList = [[random.randint(0, 1) for _ in range(length)] for _ in range(length)]

# Function to update and display the grid
def update_grid():
    wn.tracer(0)
    while True:
        FriendList = [[0 for _ in range(length)] for _ in range(length)]
        Display = []

        # Clear the previous stamps (dots) without causing an error
        t.clearstamps()

        for x in range(length):
            Display.append("\n")
            for y in range(length):
                cell = CellList[x][y]
                neighbors = (
                    CellList[(x - 1) % length][(y - 1) % length]
                    + CellList[(x - 1) % length][y]
                    + CellList[(x - 1) % length][(y + 1) % length]
                    + CellList[x][(y - 1) % length]
                    + CellList[x][(y + 1) % length]
                    + CellList[(x + 1) % length][(y - 1) % length]
                    + CellList[(x + 1) % length][y]
                    + CellList[(x + 1) % length][(y + 1) % length]
                )

                if cell == 1:
                    if neighbors > 3 or neighbors < 2:
                        CellList[x][y] = 0
                else:
                    if neighbors == 3:
                        CellList[x][y] = 1
                Display.append("||" if CellList[x][y] == 1 else "  ")

        for y in range(length):
            for x in range(length):
                if CellList[x][y] == 1:
                    t.goto(x * 10, -y * 10)
                    t.dot(10)

        print("".join(Display))
        Display = []
        wn.update()
        time.sleep(speed)

# Call the function to start the simulation
update_grid()

