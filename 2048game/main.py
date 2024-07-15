import numpy as np

def main():
    matrix = np.zeros((4, 4), dtype=int)
    matrix = add_new_2(matrix)
    CurrentCoordinates = [0, 0]
    print("Welcome to 2048 game. \n")
    print("Use following commands: \n w : Move Up \n s : Move Down \n a : Move Left \n d : Move Right\n")
    print(f"X = {CurrentCoordinates[0]}  Y = {CurrentCoordinates[1]}")
    print_matrix(matrix)

    while True:
        if not can_add_new_2(matrix):
            print("No more moves available. Game Over!")
            break

        user_move = input("[+] Enter Your Move: ").lower()
        if user_move not in ['w', 's', 'a', 'd', ' ']:
            print("Invalid move. Please use 'w', 's', 'a', 'd', or ' ' for your move.")
            continue

        if user_move == " ":
            matrix = selected_merge(matrix, CurrentCoordinates)
            print_matrix(matrix)
        else:
            CurrentCoordinates = movement(CurrentCoordinates, user_move)
            matrix = add_new_2(matrix)
            print(f"X = {CurrentCoordinates[0]}  Y = {CurrentCoordinates[1]}")
            print_matrix(matrix)

def movement(coordinate, user_input):
    original_coordinate = coordinate[:]
    if user_input == 'w' and coordinate[0] > 0:
        coordinate[0] -= 1
    elif user_input == 's' and coordinate[0] < 3:
        coordinate[0] += 1
    elif user_input == 'a' and coordinate[1] > 0:
        coordinate[1] -= 1
    elif user_input == 'd' and coordinate[1] < 3:
        coordinate[1] += 1
    else:
        print("Wrong Input")
        return original_coordinate
    return coordinate

def selected_merge(mat, coordinates):
    r1, c1 = coordinates
    print(f"{mat[r1][c1]} is selected")
    user_input = input("[+] Select Next number: ").lower()
    next_coordinates = movement(coordinates.copy(), user_input)
    r2, c2 = next_coordinates

    if r1 == r2 and c1 == c2:
        print("Cannot merge the same cell. Please select a different direction.")
        return mat

    print(f"{mat[r2][c2]} is selected")
    if mat[r1][c1] == mat[r2][c2] and mat[r1][c1] != 0:
        mat[r2][c2] *= 2
        mat[r1][c1] = 0
    else:
        print("Cannot merge different numbers or with empty cell.")
    return add_new_2(mat)

def add_new_2(mat):
    if can_add_new_2(mat):
        r, c = np.random.randint(0, 4, size=2)
        while mat[r][c] != 0:
            r, c = np.random.randint(0, 4, size=2)
        mat[r][c] = 2
    return mat

def can_add_new_2(mat):
    return np.any(mat == 0)

def print_matrix(mat):
    for i in range(4):
        for j in range(4):
            print(f"\t{mat[i][j]}", end=" ")
        print("\n")

if __name__ == "__main__":
    main()