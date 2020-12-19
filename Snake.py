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
GRID_DIMENSION = 20 #Number of squares in the horizontal and vertical direction 

# #Class to build background/grid for screen. Not used
# class Grid():
    
#     def __init__(self, screen, thickness = 50):
#         self.screen = screen
#         self.thickness = thickness
            
    
#     def draw(self):
#         for i in range(0, WINDOW_WIDTH+1):
#             rect = pygame.Rect(i*self.thickness, 0, 1, WINDOW_HEIGHT)
#             pygame.draw.rect(screen, WHITE, rect, 0)
#         for i in range(0, WINDOW_HEIGHT+1):
#             rect = pygame.Rect(0, i*self.thickness, WINDOW_WIDTH, 1)
#             pygame.draw.rect(screen, WHITE, rect, 0)






            
#Head of a snake, in the future will add ability to interact with apples and detect collision with walls            

class Head():
    def __init__(self):
        self.loc = [random.randint(0, GRID_DIMENSION), random.randint(0, GRID_DIMENSION)] #randomly spawn the snake
        self.vel = 'Null' #controls where the head of the snake is going, starts at null (motionless)
        
    def move(self): #depending on the vel of the head, controls movement of the snake
        if self.vel == "UP":
            self.loc[1] -= 1
        if self.vel == "DOWN":
            self.loc[1] +=1
        if self.vel == "RIGHT":
            self.loc[0] +=1
        if self.vel == "LEFT":
            self.loc[0] -= 1

#Segment of the snake that will follow the head

class Segment():
    def __init__(self, head, loc, vel):
        self.head = head
        self.vel = vel #velocity of the snake segment (where is is headed)
        self.loc = loc #location of the snake segment
        self.turnQueue = [] #queue of xy coordinates and velocities, so a snake segment knows when to turn to keep following the head
        
    def move(self): #controls movement of a segment based on its velocity
            
        if self.vel == "UP":
            self.loc[1] -= 1
        if self.vel == "DOWN":
            self.loc[1] +=1
        if self.vel == "RIGHT":
            self.loc[0] +=1
        if self.vel == "LEFT":
            self.loc[0] -= 1
        
        
        
        if len(self.turnQueue) > 0 and self.turnQueue[0][0] == self.loc: #if the segment's current location is in the queue, change velocity based of the queue
            self.vel = self.turnQueue[0][1]
            self.turnQueue.pop(0)
            
        # For Debugging
        
        # print("head loc: " + str(self.head.loc))
            
        # print("item loc: " + str(self.loc))
        
        # print(self.turnQueue)
    
    def addToQueue(self, loc, direction): # create entry in queue so the segment knows when to turn
        self.turnQueue.append((loc.copy(), direction))
                
#Snake w/ head and segments

class Snake():
    def __init__(self, thickness = 20):
        self.head = Head()
        self.segments = []
        self.thickness = thickness
        
    def addSegment(self): #function for adding new segments to the head of a snake

        #bases velocity and segment based off head (if there are no other segments) or last segment
        if len(self.segments) == 0:
            newLoc = self.head.loc.copy()
            newVel = self.head.vel
            
        else:
            newLoc = self.segments[-1].loc.copy()
            newVel = self.segments[-1].vel
            
       
        if newVel == "UP":
            newLoc[1] += 1
        if newVel == "DOWN":
            newLoc[1] -=1
        if newVel == "RIGHT":
            newLoc[0] -=1
        if newVel == "LEFT":
            newLoc[0] +=1
    
            
        self.segments.append(Segment(self.head, newLoc, newVel))
        
        #copy the queue of the latest segment into this new segment so it can figure out where to turn
        if len(self.segments) > 1:
            self.segments[-1].turnQueue = self.segments[-2].turnQueue.copy()
    
        
    #Methods to change snakes direction, changes head velocity, and then adds location to segment queue so the segments know when to turn
        
    def up(self):
        if self.head.vel != "UP":
            self.head.vel = "UP"
            for part in self.segments:
                part.addToQueue(self.head.loc, "UP")
    
    def down(self):
        if self.head.vel != "DOWN":
            self.head.vel = "DOWN"
        for part in self.segments:
            part.addToQueue(self.head.loc, "DOWN")
            
    
    def right(self):
        if self.head.vel != "RIGHT":
            self.head.vel = "RIGHT"
        for part in self.segments:
            part.addToQueue(self.head.loc, "RIGHT")
            
    
    def left(self):
        if self.head.vel != "LEFT":
            self.head.vel = "LEFT"
        for part in self.segments:
            part.addToQueue(self.head.loc, "LEFT")
            
    
    #Move method to update locations
            
    def move(self):
        self.head.move()
        for part in self.segments:
            part.move()
    
    #Prints snake to terminal, probably should make this a classless method when apples are added
    def printSnakeTerminal(self):
        segmentList = []
        for part in self.segments:
            segmentList.append(part.loc)
        for y in range(0, self.thickness):
            printString = ''
            for x in range(0, self.thickness):
                if self.head.loc[0] == x and self.head.loc[1] == y:
                    printString += '*'
                elif [x,y] in segmentList:
                    printString += '+'
                else:
                    printString += 'O'
                printString += " "
            print(printString)
                
                
    
            
        
        
clock = pygame.time.Clock()
snake = Snake()

pygame.init()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
# screen.fill(BLACK)
# grid = Grid(screen)
# snake.draw()
# grid.draw()


count = 0
while True:
    clock.tick(3)
    # grid.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                snake.addSegment()
                
            if event.key == pygame.K_UP:
                snake.up()
        
               
            if event.key == pygame.K_DOWN:
                snake.down()
            if event.key == pygame.K_LEFT:
                snake.left()
            if event.key == pygame.K_RIGHT:
                snake.right()
    
    print('\n')
    print(count)
    print('\n')
    snake.move()
    snake.printSnakeTerminal()
    
    count+=1
            
                
    # pygame.display.update()