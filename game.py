import pygame
from pygame import *
import time

from variables import *

pygame.init()


class Jeu:
    def __init__(self, n_rows, n_cols):
        self.display_surface = pygame.display.get_surface()
        self.w = self.display_surface.get_width()
        self.h = self.display_surface.get_height()
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.rows = (self.h // self.n_rows)
        self.cols = (self.display_surface.get_width() // self.n_cols)

    def grille(self, grid):
        self.display_surface.fill(White)
        for row in range(self.n_rows):
            pygame.draw.line(self.display_surface, Black, (0, row * self.rows), (self.w, row * self.rows))

        for col in range(self.n_cols):
            pygame.draw.line(self.display_surface, Black, (col * self.cols, 0), (col * self.cols, self.h))

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]:
                    Rect = pygame.Rect(col * self.cols, row * self.rows, self.cols, self.rows)
                    pygame.draw.rect(self.display_surface, Black, Rect)

    def vie_mort(self, board):
        def comptage(r, c):
            compte = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if (i == r and j == c) or i < 0 or j < 0 or i == self.n_rows or j == self.n_cols:
                        continue
                    if board[i][j] in range(1, 3):
                        compte += 1

            return compte

        for r in range(self.n_rows):
            for c in range(self.n_cols):
                nei = comptage(r, c)
                if board[r][c]:
                    if nei in [2, 3]:
                        board[r][c] = 2
                elif nei == 3:
                    board[r][c] = 3

        for r in range(self.n_rows):
            for c in range(self.n_cols):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1

    time.sleep(0.4)
