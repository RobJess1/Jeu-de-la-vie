import pygame

Height: int
Widht, Height = 700, 700

n_rows = 50
n_cols = 50

grid = [[0 for i in range(n_rows)]for j in range(n_cols)]

Gris_clair = (142, 162, 198)
Gris_foncee = (86, 115, 154)
White = (255, 255, 255)
Black = (0, 0, 0)
Vert = (0, 150, 0)

grid[0][5] = 1
grid[20][5] = 1
grid[20][6] = 1
grid[20][7] = 1
grid[25][20] = 1
grid[25][22] = 1
grid[24][21] = 1
grid[24][20] = 1
grid[30][5] = 1
grid[1][5] = 1
grid[2][5] = 1
grid[3][5] = 1

surface = pygame.display.set_mode((400, 300))
surface2 = pygame.display.set_mode((400, 500))
