import pygame

pygame.init()

display_width = 1000
display_height = 700
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("The Deceiver")
SSK_logo = pygame.image.load("SSK_Logo.jpg")
pygame.display.set_icon(SSK_logo)

white = [255, 255, 255]
black = [0, 0, 0]
green = (0, 255, 0)
blue = (0, 0, 128)

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'),
             pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'),
             pygame.image.load('R8.png'),
             pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'),
            pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'),
            pygame.image.load('L8.png'),
            pygame.image.load('L9.png')]

EwalkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
              pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
              pygame.image.load('R7E.png'), pygame.image.load('R8E.png')]
EwalkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
             pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
             pygame.image.load('L7E.png'), pygame.image.load('L8E.png')]

bg_Level1 = pygame.image.load('background.jpg')
bg_Level1 = pygame.transform.scale(bg_Level1, (1000, 700))
final_Level1 = pygame.image.load('final.jpg')
final_Level1 = pygame.transform.scale(final_Level1, (1000, 700))
char_level1 = pygame.transform.scale(pygame.image.load('standing.png'), (60, 60))

char_level2 = pygame.transform.scale(pygame.image.load('standing.png'), (80, 80))
char_level3 = pygame.transform.scale(pygame.image.load('standing.png'), (80, 80))

bg_Level2 = pygame.image.load('bg.jpg')
bg_Level2 = pygame.transform.scale(bg_Level2, (1000, 700))

bg_Level3 = pygame.image.load('background.jpeg')
bg_Level3 = pygame.transform.scale(bg_Level3, (1000, 700))
safe1 = pygame.transform.scale(pygame.image.load('safe1.jpeg'), (95, 100))
safe2 = pygame.transform.scale(pygame.image.load('safe2.jpeg'), (92, 109))


class Stack:
    def __init__(self):
        self.elements = list()

    def isEmpty(self):
        return len(self.elements) == 0

    def pop(self):
        assert not self.isEmpty(), "Empty stack!"
        x = self.elements.pop()
        # self.top -= 1
        return x

    def push(self, value):
        # self.top += 1
        self.elements.append(value)


class priority_queue:
    def __init__(self):
        self.q = list()

    def __len__(self):
        return len(self.q)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, pri, item):
        new = [pri, item]
        if self.isEmpty():
            self.q.append(new)
            return
        if pri >= self.highest():
            self.q.append(new)
            return
        if pri < self.lowest():
            self.q.insert(0, new)
            return
        for i in range(0, len(self)):
            if pri < self.q[i][0]:
                self.q.insert(i, new)
                return

    def dequeue(self):
        assert not self.isEmpty(), "Empty queue!"
        a = len(self.q)
        if a > 0:
            return self.q.pop(0)

    def lowest(self):
        if not self.isEmpty():
            return self.q[0][0]

    def highest(self):
        if not self.isEmpty():
            return self.q[-1][0]

    def traverse(self):
        print(self.q)

class Zimah_level1:
    def __init__(self):
        self.x = 38
        self.y = 60
        self.vel = 2
        self.walkCount = 0
        self.left = False
        self.right = False

    def character(self, win):
        if self.walkCount + 1 > 27:
            self.walkCount = 0

        if self.left:
            win.blit(pygame.transform.scale(walkLeft[self.walkCount // 4], (60, 60)), (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(pygame.transform.scale(walkRight[self.walkCount // 4], (60, 60)), (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char_level1, (self.x, self.y))

        pygame.display.update()


class Zimah_level2:
    def __init__(self):
        self.x = 0
        self.y = 50
        self.vel = 5
        self.walkCount = 0
        self.left = False
        self.right = False

    def character(self, win):
        if self.walkCount + 1 > 27:
            self.walkCount = 0

        if self.left:
            win.blit(pygame.transform.scale(walkLeft[self.walkCount // 3], (80, 80)), (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(pygame.transform.scale(walkRight[self.walkCount // 3], (80, 80)), (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char_level2, (self.x, self.y))

        pygame.display.update()


class Zimah_level3:

    def __init__(self):
        self.x = 45
        self.y = 45
        self.vel = 5
        self.walkCount = 0
        self.left = False
        self.right = False

    def character_draw(self, win):
        if self.walkCount + 1 > 27:
            self.walkCount = 0

        if self.left:
            win.blit(pygame.transform.scale(walkLeft[self.walkCount // 3], (80, 80)), (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(pygame.transform.scale(walkRight[self.walkCount // 3], (80, 80)), (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char_level3, (self.x, self.y))

        pygame.display.update()


class Enemy_level1:
    def __init__(self, x, y, width, height, end, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.vel = vel

    def draw(self, win):
        self.move()
        if self.walkcount + 1 > 24:
            self.walkcount = 0

        if self.vel > 0:
            win.blit(pygame.transform.scale(EwalkRight[self.walkcount // 7], (self.width, self.height)),
                     (self.x, self.y))
            self.walkcount += 1
        else:
            win.blit(pygame.transform.scale(EwalkLeft[self.walkcount // 7], (self.width, self.height)),
                     (self.x, self.y))
            self.walkcount += 1

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0


class Enemy_Level2():
    def __init__(self, x, y, width, height, end, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.vel = vel

    def draw(self, win):
        self.move()
        if self.walkcount + 1 > 24:
            self.walkcount = 0

        if self.vel > 0:
            win.blit(pygame.transform.scale(EwalkRight[self.walkcount // 4], (self.width, self.height)),
                     (self.x, self.y))
            self.walkcount += 1
        else:
            win.blit(pygame.transform.scale(EwalkLeft[self.walkcount // 4], (self.width, self.height)),
                     (self.x, self.y))
            self.walkcount += 1

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0


class Enemy_level3():

    def __init__(self, x, y, end, vel):
        self.x = x
        self.y = y
        self.end = end
        self.path = [self.x, self.end]
        self.EwalkCount = 0
        self.vel = vel

    def enemy_draw(self, win):
        self.move()
        if self.EwalkCount + 1 > 24:
            self.EwalkCount = 0

        if self.vel > 0:
            win.blit(pygame.transform.scale(EwalkRight[self.EwalkCount // 4], (70, 80)), (self.x, self.y))
            self.EwalkCount += 1
        else:
            win.blit(pygame.transform.scale(EwalkLeft[self.EwalkCount // 4], (70, 80)), (self.x, self.y))
            self.EwalkCount += 1

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.EwalkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.EwalkCount = 0


class level1:
    player = Zimah_level1()
    enemy1 = Enemy_level1(370, 200, 60, 60, 600, 2)
    enemy2 = Enemy_level1(190, 340, 60, 60, 600, 2)
    enemy3 = Enemy_level1(360, 60, 60, 60, 770, 2)
    enemy4 = Enemy_level1(680, 340, 60, 60, 930, 2)
    enemy5 = Enemy_level1(350, 480, 60, 60, 780, 2)

    def wall(self):
        if self.player.y == 60 and self.player.x in range(770, 800):
            self.player.x = 770
        if self.player.x in range(600, 650) and self.player.y == 200:
            self.player.x = 600
        if self.player.x in range(680, 720) and self.player.y == 340:
            self.player.x = 680
        if self.player.x in range(780, 820) and self.player.y == 480:
            self.player.x = 780

    def stairs(self):
        keys = pygame.key.get_pressed()
        if self.player.x in range(530, 570) and self.player.y == 60:
            if keys[pygame.K_DOWN]:
                self.player.y = 200

        if self.player.x in range(530, 570):
            if keys[pygame.K_UP]:
                self.player.y = 60

        if self.player.x in range(20, 80) and self.player.y == 200:
            if keys[pygame.K_DOWN]:
                self.player.y = 340

        if self.player.x in range(20, 80) and self.player.y == 340:
            if keys[pygame.K_UP]:
                self.player.y = 200

        if self.player.x in range(370, 420) and self.player.y == 340:
            if keys[pygame.K_DOWN]:
                self.player.y = 480

        if self.player.x in range(370, 420):
            if keys[pygame.K_UP]:
                self.player.y = 340

    def enemies(self):
        if self.enemy1.x == self.player.x and self.enemy1.y == self.player.y:
            self.player.x = 38
            self.player.y = 60

        if self.enemy2.x == self.player.x and self.enemy2.y == self.player.y:
            self.player.x = 38
            self.player.y = 60

        if self.enemy3.x == self.player.x and self.enemy3.y == self.player.y:
            self.player.x = 38
            self.player.y = 60

        if self.enemy4.x == self.player.x and self.enemy4.y == self.player.y:
            self.player.x = 38
            self.player.y = 60

        if self.enemy5.x == self.player.x and self.enemy5.y == self.player.y:
            self.player.x = 38
            self.player.y = 60

    def drawings_level1(self):
        self.player.character(win)
        win.blit(bg_Level1, (0, 0))
        self.enemy1.draw(win)
        self.enemy2.draw(win)
        self.enemy3.draw(win)
        self.enemy4.draw(win)
        self.enemy5.draw(win)

    def level1(self):
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            keys = pygame.key.get_pressed()

            self.wall()
            self.stairs()
            self.enemies()
            if self.player.x in range(270, 300) and self.player.y == 60:
                self.player.x = 330

            if self.player.x in range(300, 330) and self.player.y == 60:
                self.player.x = 270

            if self.player.x in range(340, 380) and self.player.y == 200:
                self.player.x = 280

            if self.player.x in range(300, 330) and self.player.y == 200:
                self.player.x = 380

            if self.player.x in range(130, 170) and self.player.y == 340:
                self.player.x = 200

            if self.player.x in range(160, 200) and self.player.y == 340:
                self.player.x = 130

            if self.player.x in range(330, 370) and self.player.y == 480:
                self.player.x = 270

            if self.player.x in range(300, 340) and self.player.y == 480:
                self.player.x = 280
            if self.player.x in range(80, 100) and self.player.y == 480:
                win.blit(final_Level1, (0, 0))
                font = pygame.font.SysFont('Calibri', 50)
                text = font.render('MISSION ACCOMPLISHED', True, blue, green)  # create a text surface object
                textRect = text.get_rect()  # create a rectangular object for the text surface object
                textRect.center = (1000 // 2, 700 // 2)
                win.blit(text, textRect)
                pygame.time.delay(1000)
                self.player.right = False
                self.player.left = False
                run = False
                pygame.mixer.music.load(obj_stack.pop())

                level2_music = pygame.mixer.music.play(-1)
                # obj_queue.enqueue(2, level2().level2())
                x = obj_queue.dequeue()
                y = x[1]
                y.level2()

            if keys[pygame.K_LEFT] and self.player.x > 30:
                self.player.x -= self.player.vel
                self.player.left = True
                self.player.right = False
            elif keys[pygame.K_RIGHT] and self.player.x < 915:
                self.player.x += self.player.vel
                self.player.left = False
                self.player.right = True
            else:
                self.player.right = False
                self.player.left = False
                self.player.walkCount = 0
            self.drawings_level1()


class level2:

    player = Zimah_level2()
    enemy1 = Enemy_Level2(100, 50, 70, 80, 370, 5)
    enemy2 = Enemy_Level2(450, 50, 70, 80, 900, 3)
    enemy3 = Enemy_Level2(100, 200, 70, 80, 500, 5)
    enemy4 = Enemy_Level2(700, 330, 70, 80, 900, 5)
    enemy5 = Enemy_Level2(100, 330, 70, 80, 570, 5)

    def wall(self):

        if self.player.y == 50 and self.player.x in range(350, 400):
            self.player.x = 350
        if self.player.x in range(530, 550) and self.player.y == 200:
            self.player.x = 530
        if self.player.x in range(0, 160) and self.player.y == 330:
            self.player.x = 160
        if self.player.x in range(590, 650) and self.player.y == 330:
            self.player.x = 580
        if self.player.x in range(650, 700) and self.player.y == 330:
            self.player.x = 700
        if self.player.x in range(380, 450) and self.player.y == 50:
            self.player.x = 450
        if self.player.x in range(600, 625) and self.player.y == 195:
            self.player.x = 625

    def stairs(self):
        if self.player.x in range(210, 250) and self.player.y == 50 and self.keys[pygame.K_d]:
            self.player.y = 470

        if self.player.x in range(190, 220) and self.player.y == 470 and self.keys[pygame.K_u]:
            self.player.y = 50

        if self.player.x in range(0, 35) and self.player.y == 200:
            if self.keys[pygame.K_UP]:
                self.player.y = 50

        if self.player.x in range(0, 35):
            if self.keys[pygame.K_DOWN]:
                self.player.y = 200

        if self.player.x in range(800, 850) and self.player.y == 470 and self.keys[pygame.K_UP]:
            self.player.x = 210
            self.player.y = 330

        if self.player.x in range(190, 220) and self.player.y == 330 and self.keys[pygame.K_DOWN]:
            self.player.x = 810
            self.player.y = 470

        if self.player.x in range(900, 950) and self.player.y == 470:
            self.player.x = 820
            self.player.y = 330

        if self.player.x in range(800, 830) and self.player.y == 330 and self.keys[pygame.K_DOWN]:
            self.player.x = 890
            self.player.y = 470

        if self.player.x in range(430, 480) and self.player.y == 330 and self.keys[pygame.K_UP]:
            self.player.x = 525
            self.player.y = 50

        if self.player.x in range(500, 550) and self.player.y == 50 and self.keys[pygame.K_DOWN]:
            self.player.x = 455
            self.player.y = 330

        if self.player.x in range(690, 720) and self.player.y == 50 and self.keys[pygame.K_DOWN]:
            self.player.x = 710
            self.player.y = 195

        if self.player.x in range(690, 720) and self.player.y == 195 and self.keys[pygame.K_UP]:
            self.player.x = 710
            self.player.y = 50

        if self.player.x in range(890, 900) and self.player.y == 195:
            self.player.x = 880
            self.player.y = 600

        if self.player.x in range(890, 900) and self.player.y == 600:
            self.player.x = 840
            self.player.y = 195

    def enemies(self):
        if self.enemy1.x == self.player.x and self.enemy1.y == self.player.y:
            self.player.x = 0
            self.player.y = 50

        if self.enemy2.x == self.player.x and self.enemy2.y == self.player.y:
            self.player.x = 0
            self.player.y = 50

        if self.enemy3.x == self.player.x and self.enemy3.y == self.player.y:
            self.player.x = 0
            self.player.y = 50

        if self.enemy4.x == self.player.x and self.enemy4.y == self.player.y:
            self.player.x = 0
            self.player.y = 50

        if self.enemy5.x == self.player.x and self.enemy5.y == self.player.y:
            self.player.x = 0
            self.player.y = 50

    def drawings_level2(self):

        self.player.character(win)
        win.blit(bg_Level2, (0, 0))
        self.enemy1.draw(win)
        self.enemy2.draw(win)
        self.enemy3.draw(win)
        self.enemy4.draw(win)
        self.enemy5.draw(win)

    def level2(self):
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.keys = pygame.key.get_pressed()
            self.wall()
            self.stairs()
            self.enemies()

            if self.player.x in range(40, 60) and self.player.y == 50:
                self.player.x = 80

            if self.player.x in range(60, 75) and self.player.y == 50:
                self.player.x = 30

            if self.player.x in range(0, 100) and self.player.y in range(500, 700):
                font = pygame.font.SysFont('Calibri', 50)
                text = font.render('MISSION ACCOMPLISHED', True, blue, green)  # create a text surface object
                textRect = text.get_rect()  # create a rectangular object for the text surface object
                textRect.center = (1000 // 2, 700 // 2)
                win.blit(text, textRect)
                pygame.time.delay(1000)
                self.player.right = False
                self.player.left = False
                run = False

                pygame.mixer.music.load(obj_stack.pop())
                level3_music = pygame.mixer.music.play(-1)

                # obj_queue.enqueue(3, level3().level3())
                x = obj_queue.dequeue()
                y = x[1]
                y.level3()

            if self.keys[pygame.K_LEFT] and self.player.x > 0:
                self.player.x -= self.player.vel
                self.player.left = True
                self.player.right = False
            elif self.keys[pygame.K_RIGHT] and self.player.x < 900:
                self.player.x += self.player.vel
                self.player.left = False
                self.player.right = True
            else:
                self.player.right = False
                self.player.left = False
                self.player.walkCount = 0
            self.drawings_level2()


class level3:
    player = Zimah_level3()                             #Enemy(starting x coord,y coord,stopping coord,speed of enemy)
    enemy1 = Enemy_level3(620, 45, 780, 5)              #1st floor
    enemy2 = Enemy_level3(445, 330, 895, 5)             #3rd floor
    enemy3 = Enemy_level3(306, 465, 890, 5)             #4th floor
    enemy4 = Enemy_level3(20, 465, 240, 5)              #4th floor left
    enemy5 = Enemy_level3(20, 185, 444, 5)              #2nd floor left
    enemy6 = Enemy_level3(500, 600, 890, 5)             #5th floor right

    def wall_constraints(self):
        if self.player.x > 785 and self.player.y == 45:                     #1st floor
            self.player.x = 784
        elif self.player.x in range(530, 550) and self.player.y == 185:     #2nd floor
            self.player.x = 548
        elif self.player.x < 450 and self.player.y == 330:                  #3rd floor
            self.player.x = 449
        elif self.player.x in range(280, 310) and self.player.y == 465:     #4th floor
            self.player.x = 309
        elif self.player.x in range(380, 420) and self.player.y == 600:     #5th floor
            self.player.x = 379
        elif self.player.x in range(245, 275) and self.player.y == 465:     #4th on left
            self.player.x = 240
        elif self.player.x in range(445, 520) and self.player.y == 185:
            self.player.x = 444                                             #2nd on left

    def stairs_lifts(self):

        if self.player.x in range(680, 770) and self.player.y == 45 and self.keys[pygame.K_DOWN]:
            self.player.y = 185                                         #2nd floor landed
            self.player.x = 750
        elif self.player.x in range(680, 770) and self.player.y == 185 and self.keys[pygame.K_UP]:
            self.player.y = 45                                          #2nd to 1st
            self.player.x = 750
        elif self.player.x in range(580, 655) and self.player.y == 185 and self.keys[pygame.K_DOWN]:
            self.player.y = 330                                         #3rd floor landed
            self.player.x = 600
        elif self.player.x in range(580, 660) and self.player.y == 330 and self.keys[pygame.K_UP]:
            self.player.y = 185
            self.player.x = 600                                         #3rd to 2nd
        elif self.player.x in range(690, 770) and self.player.y == 330 and self.keys[pygame.K_DOWN]:
            self.player.y = 465
            self.player.x = 750                                         #4th landed
        elif self.player.x in range(680, 770) and self.player.y == 465 and self.keys[pygame.K_UP]:
            self.player.y = 330
            self.player.x = 750                                         #4th to 3rd
        elif self.player.x in range(310, 360) and self.player.y == 465 and self.keys[pygame.K_DOWN]:
            self.player.y = 600
            self.player.x = 324                                         #5th landed
        elif self.player.x in range(310, 360) and self.player.y == 600 and self.keys[pygame.K_UP]:
            self.player.y = 465
            self.player.x = 324                                         #5th to 4th
        elif self.player.x in range(130, 200) and self.player.y == 600 and self.keys[pygame.K_UP]:
            self.player.y = 465
            self.player.x = 160                                         #5th to 4th on left
        elif self.player.x in range(130, 200) and self.player.y == 465 and self.keys[pygame.K_DOWN]:
            self.player.y = 600
            self.player.x = 160                                         #4th to 5th on left
        elif self.player.x == self.player.vel and self.player.y == 465 and self.keys[pygame.K_LEFT]:
            self.player.y = 185
            self.player.x = 40                                          #4th to 2nd from door
        elif self.player.x == self.player.vel and self.player.y == 185 and self.keys[pygame.K_LEFT]:
            self.player.y = 465
            self.player.x = 40                                          #2nd to 4th on left
        elif self.player.x in range(350, 430) and self.player.y == 185 and self.keys[pygame.K_d]:
            self.player.y = 600
            self.player.x = 800                                         #down to 5th floor through lift
        elif self.player.x in range(780, 850) and self.player.y == 600 and self.keys[pygame.K_u]:
            self.player.y = 185
            self.player.x = 360                                         #upto 2nd floor through lift

    def enemies(self):
        if self.enemy1.x == self.player.x and self.enemy1.y == self.player.y:
            self.player.x = 45
            self.player.y = 45

        if self.enemy2.x == self.player.x and self.enemy2.y == self.player.y:
            self.player.x = 45
            self.player.y = 45

        if self.enemy3.x == self.player.x and self.enemy3.y == self.player.y:
            self.player.x = 45
            self.player.y = 45

        if self.enemy4.x == self.player.x and self.enemy4.y == self.player.y:
            self.player.x = 45
            self.player.y = 45

        if self.enemy5.x == self.player.x and self.enemy5.y == self.player.y:
            self.player.x = 45
            self.player.y = 45

        if self.enemy6.x == self.player.x and self.enemy6.y == self.player.y:
            self.player.x = 45
            self.player.y = 45

    def all_drawings(self):

        self.player.character_draw(win)
        win.blit(bg_Level3, (0, 0))
        win.blit(safe1, (500, 578))
        win.blit(safe2, (590, 570))
        self.enemy1.enemy_draw(win)
        self.enemy2.enemy_draw(win)
        self.enemy3.enemy_draw(win)
        self.enemy4.enemy_draw(win)
        self.enemy5.enemy_draw(win)
        self.enemy6.enemy_draw(win)

    def level3(self):
        run = True
        while run:

            for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
                if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
                    run = False  # Ends the game loop

            self.keys = pygame.key.get_pressed()
            self.wall_constraints()
            self.stairs_lifts()
            self.enemies()

            if self.keys[pygame.K_LEFT] and self.player.x > self.player.vel:
                self.player.x -= self.player.vel
                self.player.left = True
                self.player.right = False
            elif self.keys[pygame.K_RIGHT] and self.player.x < 900:
                self.player.x += self.player.vel
                self.player.left = False
                self.player.right = True
            else:
                self.player.right = False
                self.player.left = False
                self.player.walkCount = 0

            self.all_drawings()

            if self.player.x in range(520, 590) and self.player.y == 600:       # when locker found
                self.player.x = 589
                font = pygame.font.SysFont('Calibri', 50)
                text = font.render('MISSION ACCOMPLISHED', True, blue, green)  # create a text surface object
                textRect = text.get_rect()  # create a rectangular object for the text surface object
                textRect.center = (1000 // 2, 700 // 2)
                win.blit(text, textRect)
                pygame.time.delay(100)
                self.player.right = False
                self.player.left = False
                run = False
                for events in pygame.event.get():
                    if events == pygame.quit():
                        quit()

obj_stack = Stack()
obj_stack.push('bella_ciao_ringtone.mp3')
obj_stack.push('OneRepublic - Counting Stars.mp3')
obj_stack.push('Queen.mp3')

#obj_queue = priority_queue()


def game_intro():

    intro = True
    while intro:
        main_screen = pygame.image.load('mybg.jpg')
        main_screen = pygame.transform.scale(main_screen, (1000, 700))
        win.blit(main_screen,(0,0))
        # win.fill(blue)
        # font = pygame.font.SysFont("comicsansms", 72)
        # text = font.render("zimaH the Deciever", True, (0, 0, 0))
        # win.blit(text, (60, 0))
        # font = pygame.font.SysFont("comicsansms", 32)
        # text = font.render("Press Space For Starting the GAME", True, (0, 0, 0))
        # win.blit(text, (60, 200))
        # font = pygame.font.SysFont("comicsansms", 32)
        # text = font.render("Press ESC for QUITTING the GAME", True, (0, 0, 0))
        # win.blit(text, (60, 300))
        # font = pygame.font.SysFont("comicsansms", 40)
        # text = font.render("Another milestone by SSK Group", True, (0, 0, 0))
        # win.blit(text, (60, 580))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(510,680):
                    for y in range(270,375):
                        if pygame.mouse.get_pos() == (x,y):
                            # print(pygame.mouse.get_pos())
                            intro = False
                            pygame.mixer.music.load(obj_stack.pop())
                            level1_music = pygame.mixer.music.play(-1, 31)
                            # obj_queue.enqueue(1, level1().level1())
                            x=obj_queue.dequeue()
                            y=x[1]
                            y.level1()
                for x in range(510, 680):
                    for y in range(400, 600):
                        if pygame.mouse.get_pos() == (x, y):
                            pygame.quit()
                            quit()
                            # print(pygame.mouse.get_pos())
            #     if event.key == pygame.K_ESCAPE:
            #         pygame.quit()
            #         quit()


# obj_queue.enqueue(0,game_intro())
obj_queue = priority_queue()
obj_queue.enqueue(1, level1())
obj_queue.enqueue(2, level2())
obj_queue.enqueue(3, level3())
if __name__ == "__main__":
    print(obj_queue.q)
    game_intro()
    msg = True
    while msg:
        main_screen = pygame.image.load('finally.jpeg')
        main_screen = pygame.transform.scale(main_screen, (1000, 700))
        win.blit(main_screen,(0,0))
        pygame.display.update()
        pygame.time.delay(1000)
        msg = False