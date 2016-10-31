#Write a program to solve a Sudoku puzzle by filling the empty cells.

#Empty cells are indicated by the character '.'.

#You may assume that there will be only one unique solution.

class solution(object):
  def solve(board,ind=0):
    if ind==81:
      return True
    i=ind//9
    j=ind%9
    if board[i][j]!='.':
      return solve(board,ind+1)
    else:
      for f in [str(x) for x in range(1,10)]:
        if isValidFill(board,i，j,f):
          if j!=8:
            board[i]=board[i][:j]+f+board[i][j+1:]
          else:
            board[i]=board[i][:j]+f
          if solve(board,ind+1):
            return True
          if j !=8:
            board[i]=board[i][:j]+'.'+board[i][j+1:]
          else:
            board[i]=board[i][:j]+'.'
      return False
  def isValidFill(board,i,j,fill):
    for k in range(9):
      if board[i][k]==fill:
        return False
      if board[k][j]==fill:
        return False
      r=i//3*3+j//3
      if board[r//3*3+k//3][r%3*3+k%3]==fill:
        return False
    retur True
            
