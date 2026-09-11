import numpy as np

def create_sudoku(size):
    sudoku = np.zeros((size, size), dtype=int)
    print("Element Entry")
    while True:
        try:
            a = int(input(f"Enter the row (1-{size}): "))
            b = int(input(f"Enter the column (1-{size}): "))
            c = int(input(f"Enter the value (1-{size}): "))
            
            if 1 <= a <= size and 1 <= b <= size and 1 <= c <= size:
                sudoku[a - 1][b - 1] = c
            else:
                print(f"Values out of range. Row, column, and value must be between 1 and {size}.")
        except ValueError:
            print("Please enter valid integers.")
            continue

        d = input("Do you want to add more elements? (y/n): ").strip().lower()
        if d == 'n':
            break
            
    return sudoku

def is_valid(grid, row, col, num, box_r, box_c):
    if num in grid[row, :]:
        return False

    if num in grid[:, col]:
        return False

    start_r = (row // box_r) * box_r
    start_c = (col // box_c) * box_c
    if num in grid[start_r:start_r + box_r, start_c:start_c + box_c]:
        return False

    return True

def solve(grid, box_r, box_c):
    size = grid.shape[0]
    for r in range(size):
        for c in range(size):
            if grid[r, c] == 0:
                for num in range(1, size + 1):
                    if is_valid(grid, r, c, num, box_r, box_c):
                        grid[r, c] = num
                        if solve(grid, box_r, box_c):
                            return True
                        grid[r, c] = 0
                return False
    return True

def solve_sudoku(sudoku):
    size = sudoku.shape[0]
    box_r, box_c = (2, 3) if size == 6 else (3, 3)
    
    board_copy = sudoku.copy()
    if solve(board_copy, box_r, box_c):
        return board_copy
    else:
        print("No valid solution exists for this configuration.")
        return None

def main():
    print("1. 6x6 Sudoku")
    print("2. 9x9 Sudoku")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        sudoku = create_sudoku(6)
    elif choice == '2':
        sudoku = create_sudoku(9)
    else:
        print("Invalid choice.")
        return

    print("\nInitial Sudoku:")
    print(sudoku)

    solved_sudoku = solve_sudoku(sudoku)
    if solved_sudoku is not None:
        print("\nSolved Sudoku:")
        print(solved_sudoku)

if __name__ == "__main__":
    main()
