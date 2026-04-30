#Problem 1

principal = float(input("Input amount of money: "))
interest = float(input("Input annual interest rate as a percentage: "))
years = int(input("input number of years: "))
balance = principal

for i in range(1,years + 1):
    balance = balance * (1 + interest / 100)
    print(f"{balance:.2f}")
    
print("==========================")
#Problem 3

def transpose(matrix):
    inner = []
    outer = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            inner.append(matrix[j][i])
        outer.append(inner)
    return outer

m1 = [[1, 2, 3],
      [4, 5, 6]]

m2 = [[1, 2],
      [3, 4],
      [5, 6]]

        
print(transpose(m1))

print("===========================")

#Problem 4

def check_winner(board):
    ongoing = False
    for i in range(len(board)):
        for j in range(len(board)):
            if board[0][0] == board[1][1] == board[2][2] != " ":
                if board[0][0] == "X":
                    return "X is winner"
                else:
                    return "O is winner"
            elif board[0][2] == board[1][1] == board[2][0] != " ":
                if board[0][2] == "X":
                    return "X is winner"
                else:
                    return "O is winner"
            elif board[i][0] == board[i][1] == board[0][2] != " ":
                if board[i][2] == "X":
                    return "X is winner"
                else:
                    return "O is winner"
            elif board[0][j] == board[1][j] == board[2][j] != " ":
                if board[0][j] == "X":
                    return "X is winner"
                else:
                    return "O is winner"
            elif board[i][j] == " ":
                ongoing = True
            else:
                ongoing = False
    if ongoing == True:
        return "Game Ongoing"
    else:
        return "Draw"
    
board1 = [["X", "X", "X"],
        ["O", "O", " "],
        [" ", " ", " "]]
print(check_winner(board1))

board2 = [["X", "O", "X"],
        ["X", "O", " "],
        [" ", "O", "X"]]
print(check_winner(board2))

board3 = [["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]]
print(check_winner(board3))

board4 = [["X", "O", " "],
        [" ", "X", " "],
        [" ", " ", " "]]
print(check_winner(board4))