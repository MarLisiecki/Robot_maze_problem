maze = [[".", ".", ".", "."], [".", "x", "x", "x"], [".", ".", ".", "x"],
        ["x", "x", ".", "."]]


def print_maze(maze):
    for row in maze:
        row_print = ""
        for value in row:
            row_print += value + " "
        print(row_print)
    return


def solve_maze(maze):
    if len(maze) < 1:
        return None
    if len(maze[0]) < 1:
        return None
    return solve_maze_helper(maze, [], 0, 0)


def solve_maze_helper(maze, sol, pos_row, pos_col):
    #Get size of the maze
    num_row = len(maze)
    num_col = len(maze[0])

    # Base Case

    # Robot is already home

    if pos_row == num_row - 1 and pos_col == num_col - 1:
        return sol

    # Out of bounds
    if pos_row >= num_row or pos_col >= num_col:
        return None

    # An obstacle

    if maze[pos_row][pos_col] == "x":
        return None

    # Recursive case

    # Try going right
    sol.append("r")
    sol_going_right = solve_maze_helper(maze, sol, pos_row, pos_col + 1)

    if sol_going_right is not None:
        return sol_going_right

    # Try going down
    sol.pop()
    sol.append("d")
    sol_going_down = solve_maze_helper(maze, sol, pos_row + 1, pos_col)

    if sol_going_down is not None:
        return sol_going_down

    sol.pop()
    return None


board = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def solve(brd):
    finder = findemp(brd)
    if not finder:
        return True
    else:
        r, c = finder
    for i in range(1, 10):
        if is_valid(brd, i, (r, c)):
            brd[r][c] = i

            if solve(brd):
                return True
            brd[r][c] = 0
    return False


def is_valid(brd, n, p):
    for i in range(len(brd[0])):
        if brd[p[0]][i] == n and p[1] != i:
            return False
    for i in range(len(brd)):
        if brd[i][p[1]] == n and p[1] != i:
            return False
    bx = p[1] // 3
    by = p[0] // 3
    for i in range(by * 3, by * 3 + 3):
        for t in range(bx * 3, bx * 3 + 3):
            if brd[i][t] == n and (i, t) != p:
                return False
    return True


def print_board(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for t in range(len(brd[0])):
            if t % 3 == 0 and t != 0:
                print("| ", end="")
            if t == 8:
                print(brd[i][t])
            else:
                print(str(brd[i][t]) + "", end=" ")


def findemp(brd):
    for i in range(len(brd)):
        for t in range(len(brd[0])):
            if brd[i][t] == 0:
                return (i, t)
    return None
