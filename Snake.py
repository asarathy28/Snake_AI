# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:43:54 2020

@author: Spencer Davis
"""
import pygame
import sys
import random

BLACK = (0,0,0)
WHITE = (200, 200, 200)
GREEN = (0, 204, 0)
WINDOW_HEIGHT = 1001
WINDOW_WIDTH = 1001

class Grid():
    
    def __init__(self, screen, thickness = 50):
        self.screen = screen
        self.thickness = thickness
            
    
    def draw(self):
        for i in range(0, WINDOW_WIDTH+1):
            rect = pygame.Rect(i*self.thickness, 0, 1, WINDOW_HEIGHT)
            pygame.draw.rect(screen, WHITE, rect, 0)
        for i in range(0, WINDOW_HEIGHT+1):
            rect = pygame.Rect(0, i*self.thickness, WINDOW_WIDTH, 1)
            pygame.draw.rect(screen, WHITE, rect, 0)
            
class Snake():
    def __init__(self, thickness):
        self.xinit = random.randint(0, thickness)
        self.yinit = random.randint(0, thickness)
        self.thickness = thickness
        self.snakeArray = []
        for y in range(0, thickness):
            xArray = []
            for x in range(0, thickness):
                if x == self.xinit and y == self.yinit:
                    xArray.append(-1)
                else:
                    xArray.append(0)
            self.snakeArray.append(xArray)
    
    def up(self):
        for x in range(0, len(self.snakeArray)):
            for y in range(0, len(self.snakeArray)):
                if self.snakeArray[y][x] !=0:
                    print("hello")
                    self.snakeArray[y][x] = 1
                
    def down(self):
        for x in range(0, len(self.snakeArray)):
            for y in range(0, len(self.snakeArray)):
                if self.snakeArray[y][x] !=0:
                    self.snakeArray[y][x] = 2
    
    def left(self):
        for x in range(0, len(self.snakeArray)):
            for y in range(0, len(self.snakeArray)):
                if self.snakeArray[y][x] !=0:
                    self.snakeArray[y][x] = 3
    
    def right(self):
        for x in range(0, len(self.snakeArray)):
            for y in range(0, len(self.snakeArray)):
                if self.snakeArray[y][x] !=0:
                    self.snakeArray[y][x] = 4
                
    def move(self):
        for x in range(0, len(self.snakeArray)):
            for y in range(0, len(self.snakeArray)):
                if self.snakeArray[y][x] == 1:
                    self.snakeArray[y-1][x] = 1
                    self.snakeArray[y][x] = 0
                if self.snakeArray[y][x] == 2:
                    self.snakeArray[y+1][x] = 2
                    self.snakeArray[y][x] = 0
                if self.snakeArray[y][x] == 3:
                    self.snakeArray[y][x-1] = 3
                    self.snakeArray[y][x] = 0
                if self.snakeArray[y][x] == 4:
                    self.snakeArray[y][x+1] = 4
                    self.snakeArray[y][x] = 0
                    
    def printSnakeTerminal(self):
        for array in self.snakeArray:
            print(array)

    def draw(self):
        for x in range(0, len(self.snakeArray)):
            for y in range(0, len(self.snakeArray)):
                if self.snakeArray[y][x] != 0:
                    rect = pygame.Rect(x*self.thickness, y*self.thickness, self.thickness, self.thickness)
                    pygame.draw.rect(screen, GREEN, rect, 0)
            
        
        
clock = pygame.time.Clock()
snake = Snake(thickness=20)
snake.printSnakeTerminal()
pygame.init()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
screen.fill(BLACK)
grid = Grid(screen)
snake.draw()
grid.draw()



while True:
    clock.tick(3)
    grid.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.up()
            if event.key == pygame.K_DOWN:
                snake.down()
            if event.key == pygame.K_LEFT:
                snake.left()
            if event.key == pygame.K_RIGHT:
                snake.right()
    snake.draw()
    snake.move()
    grid.draw()
    print('\n')
    snake.printSnakeTerminal()
            
                
    pygame.display.update()