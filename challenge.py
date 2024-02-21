zz = []
# makes the box for the tic tac toe game
p1go = True
#the true false is for the turns of the players based on the last players turn in the function
w = False


#starts the game and positions the 1-9
def su():
    for x in range(0, 9):
        zz.append(str(x + 1))

#Prints the board after the su(): function
def pb():
    print( ' ' + zz[0] + '|' + zz[1] + '|' + zz[2])
    print( '--+-+--')
    print( ' ' + zz[3] + '|' + zz[4] + '|' + zz[5])
    print( '--+-+--')
    print( ' ' + zz[6] + '|' + zz[7] + '|' + zz[8])


#the cw function is checking for a win
def cw():
    if((zz[0] == zz[4] and
        zz[0] == zz[8]) or 
       (zz[2] == zz[4] and
        zz[4] == zz[6])):
        w = True
        pb()
        
        

#starts the game again
su()
#main code to run the game
while not w:
    pb()

    if p1go:
        print( "Player 1, select spot:")
    else:
        print( "Player 2, select spot:")

    try:
        y = int(input(">> "))
    except:
        print("Please enter a valid slot")
        continue
    if zz[y - 1] == 'X' or zz [y-1] == 'O':
        print("Illegal move, please try again")
        continue

    if p1go:
        zz[y - 1] = 'X'
    else:
        zz[y - 1] = 'O'

    p1go = not p1go

#another win check function
    for x in range (0,3) :
        y = x * 3
        if (zz[y] == zz[(y + 1)] and
            zz[y] == zz[(y + 2)]):
            w = True
            pb()
        if (zz[x] == zz[(x + 3)] and
            zz[x] == zz[(x + 6)]):
            w = True
            pb()

    cw()

print ("Player " + str(int(p1go + 1)) + " wins!\n")
# the end and prints player who won