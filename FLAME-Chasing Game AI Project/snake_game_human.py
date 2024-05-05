import pygame
import random
from enum import Enum
import random
from collections import namedtuple

pygame.init()
font = pygame.font.Font('arial.ttf', 25)
#font = pygame.font.SysFont('arial', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')
Point1 = namedtuple('Point1', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
NEW_CLR = (123,234,134)
BLACK = (0,0,0)

BLOCK_SIZE = 20
SPEED = 10

class SnakeGame:
    
    def __init__(self, w=600, h=600): # 640,480
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        
        # init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(0*BLOCK_SIZE), self.head.y)]
        
        self.score = 0
        self.food = None
        self.food1 = None
        self.food2 = None
        self.food3 = None
        self.food4 = None
        self._place_food()
        self._place_food1()
        self._place_food2()
        self._place_food3()
        self._place_food4()
        
    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        print("for first: ", x,y)

        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def _place_food1(self):
        x1 = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y1 = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        print("for second: ", x1, y1)

        self.food1 = Point1(x1, y1)
        if self.food1 in self.snake:
            self._place_food1()

    def _place_food2(self):
        x1 = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y1 = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        print("for second: ", x1, y1)

        self.food2 = Point1(x1, y1)
        if self.food2 in self.snake:
            self._place_food2()

    def _place_food3(self):
        x1 = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y1 = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        print("for second: ", x1, y1)

        self.food3 = Point1(x1, y1)
        if self.food3 in self.snake:
            self._place_food3()

    def _place_food4(self):
        x1 = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y1 = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        print("for second: ", x1, y1)

        self.food4 = Point1(x1, y1)
        if self.food4 in self.snake:
            self._place_food4()

    def play_step(self):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
        
        # 2. move
        self._move(self.direction) # update the head
        self.snake.insert(0, self.head)
        
        # 3. check if game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score
            
        # 4. place new food or just move
        if self.head == self.food:
            self.score -= 1
            self._place_food()
        elif self.head == self.food1:
            self.score += 1
            self._place_food1()
        elif self.head == self.food2:
            self.score += 1
            self._place_food2()
        elif self.head == self.food3:
            self.score += 1
            self._place_food3()
        elif self.head == self.food4:
            self.score += 1
            self._place_food4()
        else:
            self.snake.pop()
        
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        # 6. return game over and score
        return game_over, self.score
    
    def _is_collision(self):
        # hits boundary
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        # hits itself
        if self.head in self.snake[1:]:
            return True
        
        return False
        
    def _update_ui(self):
        self.display.fill(BLACK)
        cell_size = 40
        cell_number = 15
        screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
        nme = pygame.image.load("enemy1.png").convert_alpha()
        girl = pygame.image.load("girl3.jpg").convert_alpha()
        heart = pygame.image.load("heart4.jpg").convert_alpha()
        aff = pygame.image.load("affair.jpg").convert_alpha()
        marg = pygame.image.load("marg3.png").convert_alpha()
        boy = pygame.image.load('boy_small.png').convert_alpha()
        boy2 = pygame.image.load('boy2.png').convert_alpha()
        boy3 =pygame.image.load('boy3.png').convert_alpha()

        for pt in self.snake:
            im5 = pygame.draw.rect(self.display, BLACK, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            boy_list = [boy,boy2,boy3]
            boy_im = random.choice(boy_list)
            screen.blit(boy2, im5)

        im = pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        im1 = pygame.draw.rect(self.display, RED, pygame.Rect(self.food1.x, self.food1.y, BLOCK_SIZE, BLOCK_SIZE))
        im2 = pygame.draw.rect(self.display, RED, pygame.Rect(self.food2.x, self.food2.y, BLOCK_SIZE, BLOCK_SIZE))
        im3 = pygame.draw.rect(self.display, RED, pygame.Rect(self.food3.x, self.food3.y, BLOCK_SIZE, BLOCK_SIZE))
        im4 = pygame.draw.rect(self.display, NEW_CLR, pygame.Rect(self.food4.x, self.food4.y, BLOCK_SIZE, BLOCK_SIZE))
        screen.blit(nme, im)
        screen.blit(girl, im1)
        screen.blit(heart, im2)
        screen.blit(aff, im3)
        screen.blit(marg, im4)

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
        
    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
            
        self.head = Point(x, y)
            

if __name__ == '__main__':
    game = SnakeGame()
    
    # game loop
    while True:
        game_over, score = game.play_step()
        
        if game_over == True:
            break
        
    print('Final Score', score)
        
        
    pygame.quit()