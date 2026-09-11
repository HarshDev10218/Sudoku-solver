# 🧩 Sudoku Solver

A simple **Python-based Sudoku Solver** that allows users to create and solve **6×6 or 9×9 Sudoku puzzles** directly from the command line.

The program uses **NumPy arrays** to represent the Sudoku board and a **backtracking algorithm** to find a valid solution.

---

## ✨ Features

* 🧩 Supports **6×6 Sudoku**
* 🧩 Supports **9×9 Sudoku**
* ⌨️ Interactive command-line input
* ✅ Validates row, column, and sub-grid constraints
* 🔄 Uses recursive **backtracking** to solve the puzzle
* 🛡️ Handles invalid input and out-of-range values
* 📋 Displays both the initial and solved Sudoku boards
* ❌ Detects configurations with no valid solution

---

## 🛠️ Technologies Used

* **Python 3**
* **NumPy**
* **Recursion**
* **Backtracking Algorithm**

---

## 📁 Project Structure

```text
Sudoku-Solver/
│
├── sudoko.py
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Sudoku-Solver.git
```

### 2. Navigate to the Project

```bash
cd Sudoku-Solver
```

### 3. Install Dependencies

The project requires NumPy.

```bash
pip install numpy
```

### 4. Run the Program

```bash
python sudoko.py
```

---

## 🎮 How to Use

When the program starts, you can choose between two Sudoku sizes:

```text
1. 6x6 Sudoku
2. 9x9 Sudoku
Enter your choice (1 or 2):
```

After selecting a board size, enter the **row, column, and value** for each element.

Example:

```text
Enter the row (1-9): 1
Enter the column (1-9): 3
Enter the value (1-9): 5
```

The program then asks:

```text
Do you want to add more elements? (y/n):
```

Enter `n` when you have finished entering the puzzle.

The program displays the initial Sudoku and then attempts to solve it.

---

## 🧠 How It Works

### 1. Create the Sudoku Board

The `create_sudoku()` function creates an empty NumPy matrix and allows the user to enter values into specific positions.

### 2. Validate Possible Values

Before placing a number, `is_valid()` checks:

* Whether the number already exists in the row
* Whether the number already exists in the column
* Whether the number already exists in the corresponding sub-grid

### 3. Backtracking Solver

The `solve()` function searches for an empty cell and tries possible values from `1` through the board size.

If a choice eventually leads to an invalid configuration, the algorithm **backtracks** and tries another value.

### 4. Board-Specific Sub-Grids

The program uses:

* **2×3 boxes** for 6×6 Sudoku
* **3×3 boxes** for 9×9 Sudoku

---

## 📊 Algorithm

The solver uses **Backtracking**.

### Basic Approach

```text
Find an empty cell
       ↓
Try a possible number
       ↓
Check if the number is valid
       ↓
Place the number
       ↓
Recursively solve the remaining board
       ↓
 ┌───────────────┐
 │ Solution found │ → Yes → Return solution
 └───────────────┘
       ↓ No
Remove the number
       ↓
Try another number
```

---

## ⏱️ Complexity

For a Sudoku board of size `N × N`, backtracking has an exponential worst-case time complexity.

**Worst case:**

```text
O(N^N)
```

The actual runtime depends heavily on the number and arrangement of the initially provided values.

The solver uses additional space because of recursion and the copied Sudoku board.

---

## ⚠️ Limitations

* The program currently works only with **6×6 and 9×9** Sudoku.
* Input is entered manually through the terminal.
* There is no graphical user interface.
* The program does not provide puzzle generation.
* It does not verify whether the initial puzzle has a unique solution.
* Incorrectly entered values can overwrite existing cells.

---

## 🔮 Future Improvements

Possible improvements include:

* [ ] Add a graphical user interface
* [ ] Add Sudoku puzzle generation
* [ ] Support additional board sizes
* [ ] Add input validation for duplicate/conflicting entries
* [ ] Detect multiple solutions
* [ ] Add difficulty levels
* [ ] Add a visual solving animation
* [ ] Add a reset/restart option
* [ ] Improve the solver using heuristics such as **Minimum Remaining Values (MRV)**

---

## 📸 Screenshot

You can add a screenshot of the program here:

```markdown
## 📸 Screenshot

![Sudoku Solver Screenshot](screenshots/sudoku.png)
```

Recommended project structure:

```text
Sudoku-Solver/
│
├── sudoko.py
├── README.md
│
└── screenshots/
    └── sudoku.png
```

On GitHub, the image will appear automatically when the screenshot is committed to the repository.

---

## 👨‍💻 Author

**Harshith Dupam**

---

## ⭐ Contributing

Contributions and improvements are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

---

## 📄 License

This project is open-source and available for educational and personal use.
