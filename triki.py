from random import randrange
def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    print("+-------" * 3,"+",sep="")
    for row in range(3):
        print("|       " * 3,"|",sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ",end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    ok = False	# fake assumption - we need it to enter the loop
    while not ok:
        move = input("Ingresa tu movimiento: ")
        ok = len(move) == 1 and move >= '1' and move <= '9' # la entrada es valida?
        if not ok:
            print("movimiento equivocado - repita su movimiento!") # no, repita el movimiento
            continue
        move = int(move) - 1 	# cell's number from 0 to 8
        row = move // 3 	# cell's row
        col = move % 3		# cell's column
        sign = board[row][col]	# check the selected square
        ok = sign not in ['O','X'] 
        if not ok:	# it's occupied - to the input again
            print("Field already occupied - repeat your input!")
            continue
        board[row][col] = 'O' 	# set '0' at the selected square

def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    free = []	# the list is empty initially
    for row in range(3): # iterate through rows
        for col in range(3): # iterate through columns
            if board[row][col] not in ['O','X']: # is the cell free?
                free.append((row,col)) # yes, it is - append new tuple to the list
    return free

def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
    if sign == "X":	# are we looking for X?
        who = 'me'	# yes - it's computer's side
    elif sign == "O": # ... or for O?
        who = 'you'	# yes - it's our side
    else:
        who = None	# we should not fall here!
    cross1 = cross2 = True  # for diagonals
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:	# check row rc
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign: # check column rc
            return who
        if board[rc][rc] != sign: # check 1st diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sign: # check 2nd diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
    free = MakeListOfFreeFields(board) # make a list of free fields
    cnt = len(free)
    if cnt > 0:	# if the list is not empty, choose a place for 'X' and set it
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # make an empty board
board[1][1] = 'X' # set first 'X' in the middle
free = MakeListOfFreeFields(board)
humanturn = True # which turn is it now?
while len(free):
	DisplayBoard(board)
	if humanturn:
		EnterMove(board)
		victor = VictoryFor(board,'O')
	else:	
		DrawMove(board)
		victor = VictoryFor(board,'X')
	if victor != None:
		break
	humanturn = not humanturn		
	free = MakeListOfFreeFields(board)

DisplayBoard(board)
if victor == 'you':
	print("Ganaste!")
elif victor == 'me':
	print("Gane")
else:
	print("Empate!")