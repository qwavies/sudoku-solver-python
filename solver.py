from sudoku import print_board

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def find_empty(board):
     for i in range(len(board[0])):
          for j in range(len(board[0])):
               if board[i][j] == 0:
                    return (i, j)
               

def valid(board, number, position) -> bool:
     
     ### check row
     for i in range(len(board[0])):
          if (board[position[0]][i] == number) and (position[1] != i):
               return False