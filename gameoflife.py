
import time

def alive(cell):
    return cell == 1

def neighbours(theboard, row, col):
    size_limit = len(theboard) - 1
    alive_members = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            next_row = row + i
           # print(next_row)
            next_col = col + j
          #  print(next_col)
            if next_row == row and next_col == col:
                continue
            if next_row < 0 or next_col < 0 or next_row > size_limit or next_col > size_limit:
                continue
            if theboard[next_row][next_col] == 1:
                alive_members += 1
    return alive_members

def rules(theboard):
    new_board = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],                                  
                 [0, 0, 0, 0, 0]]

    rows = len(theboard)
    cols = len(theboard)
    for row in range(rows):
        for col in range(cols):
            if neighbours(theboard, row, col) in [2, 3] and theboard[row][col] == 1:
                new_board[row][col] = 1
            elif neighbours(theboard, row, col) == 3 and theboard[row][col] == 0:
                new_board[row][col] = 1
            else:
                new_board[row][col] = 0
    return new_board

def display(theboard):
    "Displays the alive and dead cell with unicode symbols"
    size = len(theboard)
    rows = []
    for i in range(size):
        cols = []
        for j in range(size):
#            print(theboard[i][j])
            if theboard[i][j] == 1:
                cols.append("\u25B2")
            else:
                cols.append("\u25E6")
        rows.append(" ".join(cols))
    return "\n\n".join(rows)

def main(theboard):
    for i in range(0, 10):
        print("{} generation".format(i))
        print(display(theboard))
        theboard = rules(theboard)
        time.sleep(0.5)

if __name__ == "__main__":
    theboard = [[0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

    main(theboard)