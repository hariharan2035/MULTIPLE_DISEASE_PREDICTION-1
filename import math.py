import math

B = [[" "] * 3 for _ in range(3)]

def show():
    [print(*r) for r in B]

def win():
    # Rows
    for r in B:
        if r[0] == r[1] == r[2] != " ":
            return r[0]
    # Columns
    for c in range(3):
        if B[0][c] == B[1][c] == B[2][c] != " ":
            return B[0][c]
    # Diagonals
    if B[0][0] == B[1][1] == B[2][2] != " ":
        return B[0][0]
    if B[0][2] == B[1][1] == B[2][0] != " ":
        return B[0][2]

def left():
    return any(" " in r for r in B)

def mini(d, a, b, maxi):
    w = win()
    if w == "O":
        return 10 - d
    if w == "X":
        return d - 10
    if not left():
        return 0

    if maxi:  # AI's turn (O)
        val = -math.inf
        for i in range(3):
            for j in range(3):
                if B[i][j] == " ":
                    B[i][j] = "O"
                    val2 = mini(d + 1, a, b, False)
                    B[i][j] = " "
                    val = max(val, val2)
                    a = max(a, val)
                    if b <= a:
                        return val
        return val
    else:  # Player's turn (X)
        val = math.inf
        for i in range(3):
            for j in range(3):
                if B[i][j] == " ":
                    B[i][j] = "X"
                    val2 = mini(d + 1, a, b, True)
                    B[i][j] = " "
                    val = min(val, val2)
                    b = min(b, val)
                    if b <= a:
                        return val
        return val

def best():
    mv, b = (-1, -1), -math.inf
    for i in range(3):
        for j in range(3):
            if B[i][j] == " ":
                B[i][j] = "O"
                v = mini(0, -math.inf, math.inf, False)
                B[i][j] = " "
                if v > b:
                    b, mv = v, (i, j)
    return mv

# Game loop
while not win() and left():
    show()
    x, y = map(int, input("Your move (r c): ").split())
    if B[x][y] != " ":
        print("Invalid move, try again.")
        continue

    B[x][y] = "X"
    if win() or not left():
        break

    i, j = best()
    B[i][j] = "O"
    print("AI played:")
    show()

show()
print("Winner:", win() or "Draw")
