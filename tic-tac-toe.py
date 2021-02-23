"""The player 1 starts
The program will ask a position to
the players, and they have to give a position
following this format : row,column (e.g : 2,1)
first line is 0, and first column is 0."""


class TTT(object):
    
    #create a grid and choose the current player
    def __init__(self, cp):
        
        self.grid = [[0,0,0],
                   [0,0,0],
                   [0,0,0]]
        self.cp = cp

    #Ask a position to the current player 
    def ask(self):
        pos=input("Player " + str(self.cp) + ', position ? ')
        return pos

    #check whether the position the player has given is correct or not
    #It will return a number that represents the rank of the problem encountered
    #or a string if everything is correct
    def check(self, t):
        try:
            #if the player gives a too long string
            if len(t) != 3:
                return 1
            #check if the first or the second info is greater than 2
            elif int(t[0])>2 or int(t[2])>2:
                return 1
            #check if the second character is not a ','
            elif t[1] != ',':
                return 1
        #raises an exception, when the player gives a dictionary for example    
        except:
            return 1
        x=t[0]
        y=t[2]
        if self.grid[int(x)][int(y)] != 0:
            return 2
        
        #return the position (string of 2 digits)
        else:
            return x+y

    #Put the number in the grid where c represents the postion
    #c is a string of two digits : 1st one : row, 2nd one : column
    def replace(self, c):
        x=int(c[0])
        y=int(c[1])
        self.grid[x][y] = int(self.cp)

    #recognize the problem with the number secured in self.check     
    def verif(self, t):
        if t == 1:
            return 'Please follow the rules'
        else:
            return 'The position has already been used !'

    #check if the game is finished or not
    #if the game is finished, return True, else return False
    def finish(self):
        _ = self.grid
        #verify the equality of the numbers in the same diagonal, and confirm they are different to 0
        if (_[0][0] == _[1][1] == _[2][2] and _[0][0] != 0) or (_[0][2] == _[1][1] == _[2][0] and _[0][2] != 0):
            return True
        for a in range(3):
            #check if all the digits are the same and different to 0 in the same line
            r = all(elm == _[a][0] != 0 for elm in _[a])
            if r:
                return True

            #check if all the digits are the same and different to 0 in the same column
            rr=all(elm == _[0][a] != 0 for elm in [h[0] for h in _])
            if rr:
                return True
        #If all of the digits are not the same in a diagonal, column or a line, return False  
        return False
        
                  
    #switch the player    
    def switch(self):
        if self.cp == 1:
            self.cp=2
        else:
            self.cp=1
        

#Function called to start a game, with cp as a parameter (current player or first player)
def startGame(cp):
    #create a variable f that represents the number of replacements in the grid
    #When 9=0, the game is over
    f=0

    #create a game
    a=TTT(cp)

    #if the game is not finish and f is not equal to 9
    while a.finish() == False and f != 9:

        #when the game starts, we don't need to switch the player
        if f != 0:
            a.switch()

        #display the grid
        print(a.grid)
        num_p = 3

        #when num_p is a digit, it means that there is a problem
        #it means that the player didn't submit a correct position
        while type(num_p) != str:

            #ask a position to the player
            pos = a.ask()
            num_p = a.check(pos)
            if type(num_p) == int:
                print(a.verif(num_p))

        #if there is no problem, replace 0 by the player number in the grid at the assigned postion    
        a.replace(num_p)

        #add 1 to the number of substitutions
        f += 1

    #when the game is finished, display the grid
    print(a.grid)

    #if we have the same numbers but 0 in the same column, line or diagonal
    #else, there is no winner
    if a.finish() == True:
        print('Player ' + str(a.cp) + ' is the winner !')
    else:
        print('No winner')

startGame(1)
            
        
    
    
