import pygame
from pygame import MOUSEBUTTONDOWN
import random
from random import randint

from variables import *
from game import Jeu
import time
from Bouton import *

pygame.init()

Fenetre = pygame.display.set_mode((Widht, Height))
pygame.display.set_caption('Jeu de la Vie ')
temps = pygame.time.Clock()


def menu():
    run = True
    FPS = 60
    new_Game = Jeu(n_rows, n_cols)
    pause = False
    t = 0.3

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mox = event.pos[0]
                moy = event.pos[1]
                print(mox, moy)
                print(new_Game.cols, new_Game.rows)
                idx = mox // new_Game.cols
                idy = moy // new_Game.rows
                print(idx, idy)
                grid[idy][idx] = abs(grid[idy][idx] - 1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    random_init(grid)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    t = t - 0.1
                    if t < 0.0:
                        t = 0.01

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    t = t + 0.1
                    if t > 3:
                        t = 2.9

        new_Game.grille(grid)
        if not pause:
            time.sleep(t)
            new_Game.vie_mort(grid)

        pygame.display.update()
        temps.tick(FPS)


def random_init(gr_de_travail):
    for row in range(len(gr_de_travail)):
        for col in range(len(gr_de_travail[row])):
            gr_de_travail[row][col] = random.randint(0, 1)


menu()
