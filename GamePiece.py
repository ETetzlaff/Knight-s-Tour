import sys
import time
board = []          #number list to print out
n = 8       #this is the size of the board
max = (n**2)-1   #this is move cap, which will be used to check and ensure we don't go over
m = 0       #movement count
possibleMoves =[[-2,-1],[-1,-2],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]    #list of possible moves
t2 = 0

def createBoard(n):     #create board with nxn
    for i in range(n):
        board.append([])
        for a in range(n):
            board[i].append(0)

def checkMove(x, y):        #Ensure move has not been taken and is in bounds
    return x >= 0 and x < n and y >= 0 and y < n and board[x][y] == 0

def printBoard():
    for i in range(n):
        for a in range(n):
            print "%2d" % board[i][a],
        print
    print
    print '______________________'
        
def makeMove(x, y, m):
    
    board[x][y] = m     #setting board coordinates to move number to show steps
   
    if m == max:        #check if m is max, if it is, then program is done and successful
        printBoard()
        print 'A successful move has been found!'
        t2 = time.clock()
        print (t2-t1)*1000.00
        sys.exit(1)
      
    for move in possibleMoves:      #begin the recursive call which "iterates" through possible list
        px = x + move[0]            #possiblex will be current x + move x coord
        py = y + move[1]            #possibley will be current y + move y coord
        if (checkMove(px, py)):     #if possiblex and possibley are in bounds, then call self
            makeMove(px, py, m+1)   
            
    board[x][y] = 0 #if loops gets here, then reset coordinate and move back     
t1 = time.clock()
createBoard(n)
makeMove(0, 0, 0)
