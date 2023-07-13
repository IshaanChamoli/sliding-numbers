# need to make movement based on arrow keys instead of text!!

blankX = 0 #have to make it dynamic if I want different "start states"
blankY = 3
correct = False

def switch (onex, oney, twox, twoy):
    buffer = ostate[onex][oney]
    ostate[onex][oney] = ostate[twox][twoy]
    ostate[twox][twoy] = buffer

def print_puzzle ():
    print("")
    for k in range(24):
        print("-", end="")
    print("")

    for i in range(4):
        for j in range(4):
            if(ostate[i][j] != "_"):
                num = int(ostate[i][j])
                if(num/10 >= 1):
                    print("| ", end="")
                    print(num, end="")
                    print(" |", end="")
                    
                else:
                    print("|  ", end="")
                    print(num, end="") 
                    print(" |", end="")    
            else:
                print("|  ", end="")
                print("_", end="")
                print(" |", end="")
        print("")
        for k in range(24):
            print("-", end="")
        print("")
    

def move_up():

    switch(blankX, blankY, blankX-1, blankY)


def move_down():
    switch(blankX, blankY, blankX+1, blankY)


def move_left():
    switch(blankX, blankY, blankX, blankY-1)
   

def move_right():
    switch(blankX, blankY, blankX, blankY+1)




#------------------------------------------------------------------------------
print("\nWelcome to my Sliding Puzzle!\nSlide the numbers to the blank space - \nGet them in the right order from 1-15 (top to bottom) and win!!!!")


ostate = [
        ["10", "9", "3", "_"],
        ["2", "5", "15", "7"],
        ["8", "14", "1", "11"],
        ["12", "13", "4", "6"]
    ]


'''
easy_ostate = [                     (for testing)
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "_", "14", "15"]
    ]
'''


correct_state = [
        ["1", "2", "3", "4"],
        ["5", "6", "7", "8"],
        ["9", "10", "11", "12"],
        ["13", "14", "15", "_"]
    ]

print_puzzle()

while (True):
    print("")
    print("Type up, down, left, or right to move")
    move = input("Enter: ")
        
    if (move.upper()=="UP"):
        if(blankX == 0):
            print("\n***MOVE NOT POSSIBLE (the empty space is already at the top)")
        else: 
            move_up()
            print_puzzle()
            blankX = blankX - 1
            if(ostate == correct_state):
                break;

    elif (move.upper()=="DOWN"):
        if(blankX == (len(ostate)-1)):
            print("\n***MOVE NOT POSSIBLE (the empty space is already at the bottom)")
        else: 
            move_down()
            print_puzzle()
            blankX = blankX + 1
            if(ostate == correct_state):
                break;

    elif (move.upper()=="LEFT"):
        if(blankY == 0):
            print("\n***MOVE NOT POSSIBLE (the empty space is already on the left edge)")
        else:
            move_left()
            print_puzzle()
            blankY = blankY - 1
            if(ostate == correct_state):
                break;

    elif (move.upper()=="RIGHT"):
        if(blankY == (len(ostate[0])-1)):
            print("\n***MOVE NOT POSSIBLE (the empty space is already on the right edge)")
        else:
            move_right()
            print_puzzle()
            blankY = blankY + 1
            if(ostate == correct_state):
                break;

    else:
        print("Invalid Input (up/down/left/right)")



print("\n********************\n\nCongratulations!! Puzzle Complete! All numbers are in order :)\n")
