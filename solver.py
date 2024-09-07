# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]


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
     
     ### check column
     for i in range(len(board)):
          if (board[i][position[1]] == number) and (position[0] != i):
               return False
          
     ### check 3x3 box
     box_x, box_y = position[1] // 3 , position[0] // 3

     for i in range(box_y * 3 , box_y * 3 + 3):
          for j in range(box_x * 3 , box_x * 3 + 3):
               if board[i][j] == number and (i,j) != position:
                    return False
               
     ### passes all checks
     return True

def solve(board):
     ### base case - When board is full:
     find = find_empty(board)
     if not find:
          return True
     else:
          row, column = find

     for i in range(1,10):
          if valid(board, i , (row,column)):
               board[row][column] = i

               ### fill next empty recursively
               if solve(board):
                    return True
               
               board[row][column] = 0
     
     return False

