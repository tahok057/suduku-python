import random


class Sudoku:
    def __init__(self):
        self.grid = [[0] * 9 for _ in range(9)]
        self.generate_puzzle()

    def generate_puzzle(self):
        self.fill_grid()
        self.remove_numbers()

    def fill_grid(self):
        self._fill_grid_helper(0, 0)

    def _fill_grid_helper(self, row, col):
        if row == 9:
            return True
        if col == 9:
            return self._fill_grid_helper(row + 1, 0)

        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for num in numbers:
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num
                if self._fill_grid_helper(row, col + 1):
                    return True
                self.grid[row][col] = 0

        return False

    def remove_numbers(self):
        attempts = 5
        while attempts > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.grid[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            backup = self.grid[row][col]
            self.grid[row][col] = 0

            copy_grid = [row[:] for row in self.grid]
            if not self._has_unique_solution(copy_grid):
                self.grid[row][col] = backup
                attempts -= 1

    def is_valid_move(self, row, col, num):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def check_victory(self):
        for row in self.grid:
            if any(cell == 0 for cell in row):
                return False
        return True

    def _has_unique_solution(self, grid):

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        for num in range(1, 10):
                            if self.is_valid_move(i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                board[i][j] = 0
                        return False
            return True

        solutions = 0

        def count_solutions(board):
            nonlocal solutions
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        for num in range(1, 10):
                            if self.is_valid_move(i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    solutions += 1
                                board[i][j] = 0
                        return
            solutions += 1

        count_solutions(grid)
        return solutions == 1
