# Gravity Simulation of Falling Boxes and Exploding Obstacles

This repository contains a solution for simulating the behavior of boxes falling under gravity on a 2D grid with obstacles that trigger explosions.

## Problem Description

You are given a rectangular matrix `board` representing a simulation scenario. Each cell in `board` contains one of three characters:

* `-` : an empty space
* `*` : an obstacle
* `#` : a box

All boxes fall downward simultaneously until one of the following occurs:

1. A box reaches the bottom of the board.
2. A box lands on top of another grounded box.
3. A box encounters an obstacle.

When a box hits an obstacle, it explodes along with any other boxes in the eight neighboring cells surrounding the obstacle. All explosions occur simultaneously, and obstacles remain intact (i.e., they are not consumed by explosions).

Your task is to compute and return the final state of the board after all boxes have fallen and all explosions have resolved.

> **Note:** An optimal solution is not required. Any algorithm with time complexity up to O(`m * n^2`), where `m = board[0].length` and `n = board.length`, will run within the given limits.

---

## Examples

### Example 1

```plaintext
Input:
board = [
  ['#', '-', '#', '#', '*'],
  ['#', '-', '-', '#', '#'],
  ['-', '#', '-', '#', '-'],
  ['-', '-', '#', '-', '#'],
  ['#', '*', '-', '-', '-'],
  ['-', '-', '*', '#', '-']
]

Output:
[
  ['-', '-', '-', '-', '*'],
  ['-', '-', '-', '-', '-'],
  ['-', '-', '-', '-', '-'],
  ['-', '-', '-', '-', '-'],
  ['-', '*', '-', '-', '#'],
  ['#', '-', '*', '-', '#']
]
```

### Example 2

```plaintext
Input:
board = [
  ['#', '#', '*'],
  ['#', '-', '*'],
  ['#', '-', '*'],
  ['-', '#', '#'],
  ['*', '-', '#'],
  ['*', '-', '-'],
  ['*', '-', '-']
]

Output:
[
  ['-', '-', '*'],
  ['-', '-', '*'],
  ['-', '-', '*'],
  ['-', '-', '-'],
  ['*', '-', '-'],
  ['*', '-', '#'],
  ['*', '-', '#']
]
```

---

## Input/Output Specification

* **Input**: A 2D array `board` of characters (`'-'`, `'*'`, `'#'`).
* **Output**: A 2D array of the same dimensions representing the board state after simulation.

**Constraints:**

* `3 ≤ board.length ≤ 100`
* `3 ≤ board[i].length ≤ 100`

**Execution Limits:**

* Time: 0.5 seconds (C++)
* Memory: 1 GB

---

## Usage

Implement your solution in C++ (or your preferred language) and ensure it reads from standard input and writes the resulting board to standard output in the same format.

```cpp
// Example function signature:
vector<vector<char>> solution(vector<vector<char>>& board);
```

---

## License

This project is licensed under the MIT License. Feel free to use and modify as needed.
