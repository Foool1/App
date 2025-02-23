import random

def printing(table):
    for i in range(3):
        for j in range(3):
            print(f"|{table[i][j]}", end="")
        print("|", end="")
        print("")

def showBoard():
    x = 0
    for i in range(3):
        for j in range(3):
            print(f"|{x}", end="")
            x+=1
        print("|", end="")
        print("")

def ai(table):
    x = random.randint(0,2)
    y = random.randint(0,2)
    while table[x][y] != ' ':
        x = random.randint(0,2)
        y = random.randint(0,2)
    table[x][y] = 'X'
        

def game(table):
    while any(' ' in row for row in table):
        print("press the number where u want to put your \"O\" character: ", end="")
        check = 1
        while check == 1:
            player = 9
            while player not in range(9):
                player = int(input())
                if player not in range(9):
                    print("You enter wrong input, try again")

            fdigit = player / 3
            sdigit = player % 3
            if table[int(fdigit)][int(sdigit)] == ' ':
                table[int(fdigit)][int(sdigit)] = "O"
                check = 0
            else:
                print("This possition is taken, try again")
        printing(table)
        if winning(table) == True:
            print("You won!")
            return True
        elif winning(table) == False:
            print("You lost!")
            return False
        if draw(table) == True:
            print("It is a draw!")
            return True        
        print("AI move: ")
        ai(table)
        printing(table)
        if winning(table) == True:
            print("You won!")
            return True
        elif winning(table) == False:
            print("You lost!")
            return False

def winning(table):
#row:
    result = ""
    for i in range(3):
        for j in range(3):
            result += table[i][j]
        if result == "OOO":
            return True
        elif result == "XXX":
            return False
        result = ""
#column:
    result = ""
    for i in range(3):
        for j in range(3):
            result += table[j][i]
        if result == "OOO":
            return True
        elif result =="XXX":
            return False
        result = ""
#diagonal
    result = ""
    for i in range(3):
        result += table[i][i]
    if result == "OOO":
        return True
    elif result == "XXX":
        return False
    result = ""
    for i in range(3):
        result += table[i][2-i]
    if result == "OOO":
        return True
    elif result == "XXX":
        return False
    result = ""

def draw(table):
    for i in range(3):
        for j in range(3):
            if table[i][j] == ' ':
                return False
    return True

table = [[' '] * 3 for _ in range(3)] 
print("Welcome in TicTacToe game, thats how positions on board looks like: ")
showBoard()
game(table)