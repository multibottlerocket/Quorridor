import sys, math

class Game():
    def __init__(self, totalPlayers):
        self.board = Board(9,9)
        self.players = [None]
        for playerNumber in range(1, totalPlayers+1):
            self.addPlayer(playerNumber, totalPlayers)
        self.gameOver = False
        self.playerTurn = 1
 
    def addPlayer(self, playerNumber, totalPlayers):
        self.players.append(Player(playerNumber, totalPlayers))
        if playerNumber == 1:
            self.board.pieceBoard[1][self.board.boardWidth/2 + 1] = '1'
            self.players[1].xPos = self.board.boardWidth/2 + 1
            self.players[1].yPos = 1
        elif playerNumber == 2:
            self.board.pieceBoard[-2][self.board.boardWidth/2 + 1] = '2'
            self.players[2].xPos = self.board.boardWidth/2 + 1
            self.players[2].yPos = self.board.boardHeight
        elif playerNumber == 3:
            self.board.pieceBoard[self.board.boardHeight/2 + 1][1] = '3'
            self.players[3].xPos = 1
            self.players[3].yPos = self.board.boardHeight/2 + 1
        elif playerNumber == 4:
            self.board.pieceBoard[self.board.boardHeight/2 + 1][-2] = '4'
            self.players[4].xPos = self.board.boardWidth 
            self.players[4].yPos = self.board.boardHeight/2 + 1
        else:
            print 'invalid player number'
   
    def takeTurn(self):
        #offer player to move or place wall (if he has walls)
        #once player does something successfully, check for victory and increment turn counter if no victory
        return None

    def victory(self):
        #end game and declare victory for self.playerTurn
        return None

class Board():
    def __init__(self, height, width):
        self.boardHeight = height
        self.boardWidth = width
        self.pieceBoard = self.makePieceBoard(height, width)
        self.hWallBoard = self.makeWallBoard(height+1, width)
        self.vWallBoard = self.makeWallBoard(height, width+1)

    def displayBoard(self):
        sys.stdout.write(self.pieceBoard[0][0])                 #first row
        for square in self.pieceBoard[0][1:]:                   #
            sys.stdout.write(' ')                               #
            sys.stdout.write(square)                            #
        sys.stdout.write('\n')                                  #
        for row in range(self.boardHeight):                     #middle rows
            sys.stdout.write('  ')                              #
            for col in self.hWallBoard[row]:                    #  hwalls
                sys.stdout.write(col)                           #
                sys.stdout.write(' ')                           #
            sys.stdout.write(' \n')                             #
            for col in range(self.boardWidth + 1):              #  pieces and vwalls
                sys.stdout.write(self.pieceBoard[row+1][col])   #
                sys.stdout.write(self.vWallBoard[row][col])     #
            sys.stdout.write(self.pieceBoard[row][-1])          #
            sys.stdout.write('\n')                              #
        sys.stdout.write('  ')                                  #last hwall row
        for square in self.hWallBoard[-1]:                      #
            sys.stdout.write(square)                            #
            sys.stdout.write(' ')                               #
        sys.stdout.write(' \n')                                 #
        sys.stdout.write(self.pieceBoard[-1][0])                #last board row
        for square in self.pieceBoard[-1][1:]:                  #
            sys.stdout.write(' ')                               #    
            sys.stdout.write(square)                            #

    def makePieceBoard(self, height, width):
        board = [['0']*(width+2) for i in range((height+2))]  
        board[0][0]     = 'x'  # make corners out of bounds
        board[0][-1]    = 'x'
        board[-1][0]    = 'x'
        board[-1][-1]   = 'x'
        for col in range(width): #set endzones
            board[0][col+1] = 'e'
            board[-1][col+1] = 'e'
        for row in range(height):
            board[row+1][0] = 'e'
            board[row+1][-1] = 'e'
        return board
    
    def makeWallBoard(self, height, width):
        return [[' ']*width for i in range(height)]

    def movePiece(self, playerNumber, direction):
        #is wall blocking?
            #if not, is space empty?
                #if 0, move and update
                #if out of bounds and victory, move, update, and win
                #if out of bounds and not victory, request a new move
                #if other player is there, double jump
            #if blocking, request a new move

        return None

    def placeWall(self, playerNumber, wallType, xPos0, yPos0, xPos1, yPos1):
        #does the player have walls left?
            #if not, request a new move
        #is another wall in the way?
            #if so, request new move
        #does the wall block the other player from his endzone?
            #if so, request a new move
        #if all conditions met, place wall and decrement wall count for player
        return None

    def floodFill(self):
        return None

class Player():
    def __init__(self, playerNumber, totalPlayers):
        self.playerNumber = playerNumber
        self.wallCount = int(math.ceil(20.0 / totalPlayers))
        self.xPos = None
        self.yPos = None

totalPlayers = 4
game = Game(totalPlayers)
game.board.displayBoard()
