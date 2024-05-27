try:
    import pygame.event
    import time
    import random
    import sys
    import pygame.sprite
    import pygame
    from pas.pas import *
    p = input("请输入密码：")
    if p == password:
        print("正确！")
    else:
        print("错误！")
        sys.exit()

    pygame.init()

    w, h = 2000, 1000
    bg_colour = pygame.Color(0, 0, 0)
    text_colour = pygame.Color(255, 0, 0)
    good_color = (0, 255, 0)
    bad_color = (255, 0, 0)

    class BaseItem(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            pygame.sprite.Sprite.__init__(self)


    class MainGame:
        window = None
        my_tank = None
        enemyTankList = []
        while True:
            try:
                while True:
                    enemyTankCount = int(input("一共多少个坦克(推荐5以上500以下）（1000以下）："))
                    if enemyTankCount <= 4 or enemyTankCount > 1000:
                        print("您输入的数字超出了范围，请重新输入。")
                        continue
                    else:
                        break
                break
            except ValueError:
                print("您输入的并不是数字，请重新输入。")
        myBulletList = []
        enemyBulletList = []
        explode_list = []
        Wall1List = []
        Wall2List = []
        font_new = pygame.font.Font("C:/Windows/Fonts/simkai.ttf", 70)
        while True:
            try:
                while True:
                    level = int(input("请输入您想要的难度(推荐1~10)(10000以下)："))
                    if level < 1 or level > 10000:
                        print("您输入的不在范围内，请重新输入。")
                        continue
                    else:
                        break
                break
            except ValueError:
                print("您输入的不是数字，请重新输入。")
                continue
        while True:
            try:
                while True:
                    my_tank_live = int(input("设置有几条命(-1就是无限）：")) - 1
                    if level == 0 or level < -2:
                        print("您输入的数字比0小，请重新输入。")
                        continue
                    else:
                        break
                break
            except ValueError:
                print("您输入的并不是数字，请重新输入。")

        def __init__(self):
            pass

        def start_game(self):
            import pygame
            pygame.display.init()
            MainGame.window = pygame.display.set_mode((w, h))
            self.create_my_tank()
            self.create_enemy_tank()
            self.create_wall()
            pygame.display.set_caption("坦克大战")
            while True:
                time.sleep(0.03)
                MainGame.window.fill(bg_colour)
                self.get_event()
                MainGame.window.blit(self.text("剩余敌方坦克数量：%d " % len(MainGame.enemyTankList)), (10, 10))
                MainGame.window.blit(self.text("我方子弹数量：%d" % len(MainGame.myBulletList)), (210, 10))
                MainGame.window.blit(self.text("敌方子弹数量：%d" % len(MainGame.enemyBulletList)), (410, 10))
                if MainGame.my_tank_live != -2:
                    MainGame.window.blit(self.text("剩余%d条命" %(MainGame.my_tank_live)), (10, 50))
                if len(MainGame.enemyTankList) == 0:
                    MainGame.window.blit(self.text_new("闯关成功！"), (200, 10))
                    MainGame.enemyTankList.clear()
                    print("闯关成功！")
                    time.sleep(2)
                    input("按任意键退出：")
                    MainGame.endgame()
                if MainGame.my_tank_live + 1 == 0:
                    MainGame.window.blit(self.text_new_new("Game Over！"), (w / 2, h / 2))
                    MainGame.enemyTankList.clear()
                    print("Game Over!")
                    time.sleep(2)
                    input("按任意键退出：")
                    MainGame.endgame()
                if MainGame.my_tank and MainGame.my_tank.live:
                    MainGame.my_tank.display_tank()
                else:
                    del MainGame.my_tank
                    MainGame.my_tank = None
                self.blit_enemy_tank()
                self.blit_my_bullet()
                self.blit_enemy_bullet()
                self.blit_explode()
                self.blitWall1()
                if MainGame.my_tank and MainGame.my_tank.live:
                    if not MainGame.my_tank.stop:
                        MainGame.my_tank.move()
                        MainGame.my_tank.hit_wall()
                        MainGame.my_tank.my_tank_and_enemy_tank_in_a_space()
                pygame.display.update()

        def create_my_tank(self):
            MainGame.my_tank = MyTank(700, 700)
            self.stop = True

        @staticmethod
        def create_enemy_tank():
            for i in range(MainGame.enemyTankCount):
                left = random.randint(0, w)
                top = random.randint(0, h)
                speed = random.randint(1, 4)
                enemy = EnemyTank(left, top, speed)
                MainGame.enemyTankList.append(enemy)

        def blitWall1(self):
            for wall in MainGame.Wall1List:
                if wall.live:
                    wall.display_wall()
                else:
                    MainGame.Wall1List.remove(wall)

        def create_wall(self):
            for i in range(100, 900, 25):
                wall = Wall1(50, i)
                MainGame.Wall1List.append(wall)
            for i in range(100, 400, 50):
                wall = Wall1(i, 500)
                wall2 = Wall1(i, 525)
                MainGame.Wall1List.append(wall)
                MainGame.Wall1List.append(wall2)
            for i in range(100, 550, 25):
                wall = Wall1(400, i)
                MainGame.Wall1List.append(wall)
            for i in range(100, 400, 25):
                wall = Wall1(i, 100)
                MainGame.Wall1List.append(wall)
            for i in range(100, 900, 25):
                wall = Wall1(500, i)
                MainGame.Wall1List.append(wall)
            for i in range(500, 900, 25):
                wall = Wall1(i, 900)
                MainGame.Wall1List.append(wall)
            for i in range(500, 900, 25):
                wall = Wall1(i, 875)
                MainGame.Wall1List.append(wall)
            for i in range(100, 900, 25):
                wall = Wall1(1000, i)
                MainGame.Wall1List.append(wall)
            for i in range(100, 150, 25):
                for j in range(1025, 1400, 25):
                    wall = Wall1(j, i)
                    MainGame.Wall1List.append(wall)
            for i in range(100, 900, 25):
                wall = Wall1(1375, i)
                MainGame.Wall1List.append(wall)
            for i in range(500, 550, 25):
                for j in range(1025, 1400, 25):
                    wall = Wall1(j, i)
                    MainGame.Wall1List.append(wall)
            for j in range(1500, 2300, 400):
                for i in range(100, 525, 25):
                    wall = Wall1(j, i)
                    MainGame.Wall1List.append(wall)
            for i in range(475, 525, 25):
                for j in range(1500, 1925, 25):
                    wall = Wall1(j, i)
                    MainGame.Wall1List.append(wall)
            for i in range(500, 900, 25):
                wall = Wall1(1700, i)
                MainGame.Wall1List.append(wall)

        @staticmethod
        def blit_explode():
            for explode in MainGame.explode_list:
                if explode.live:
                    explode.display_explode()
                else:
                    MainGame.explode_list.remove(explode)

        @staticmethod
        def blit_enemy_tank():
            for enemyTank in MainGame.enemyTankList:
                if enemyTank.live:
                    enemyTank.display_tank()
                    enemyTank.rand_move()
                    enemyTank.hit_wall()
                    if MainGame.my_tank and MainGame.my_tank.live:
                        enemyTank.enemy_tank_and_my_tank_in_a_space()
                    enemy_bullets = enemyTank.shot()
                    if enemy_bullets:
                        MainGame.enemyBulletList.append(enemy_bullets)
                else:
                    MainGame.enemyTankList.remove(enemyTank)

        @staticmethod
        def blit_my_bullet():
            for myBullet in MainGame.myBulletList:
                if myBullet.live:
                    myBullet.display_bullets()
                    myBullet.move()
                    myBullet.my_bullets_hit_enemy_tank()
                    myBullet.hit_wall()
                else:
                    MainGame.myBulletList.remove(myBullet)

        def blit_enemy_bullet(self):
            for enemy_Bullet in MainGame.enemyBulletList:
                if enemy_Bullet.live:
                    enemy_Bullet.display_bullets()
                    enemy_Bullet.move()
                    enemy_Bullet.enemy_bullets_hit_my_tank()
                    enemy_Bullet.hit_wall()

                else:
                    MainGame.enemyBulletList.remove(enemy_Bullet)

        @staticmethod
        def endgame():
            pygame.quit()
            sys.exit()

        @staticmethod
        def text(text):
            pygame.font.init()
            font = pygame.font.SysFont("kaiti", 20)
            text_surface = font.render(text, True, text_colour)
            return text_surface

        @staticmethod
        def text_new(text):
            pygame.font.init()
            text_surface_new = MainGame.font_new.render(text, True, good_color)
            return text_surface_new

        @staticmethod
        def text_new_new(text):
            pygame.font.init()
            text_surface_new_new = MainGame.font_new.render(text, True, bad_color)
            return text_surface_new_new

        def get_event(self):
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    self.endgame()
                if event.type == pygame.KEYDOWN:
                    if not MainGame.my_tank:
                        if event.key == pygame.K_ESCAPE:
                            if MainGame.my_tank_live == -2:
                                self.create_my_tank()
                            else:
                                self.create_my_tank()
                                MainGame.my_tank_live -= 1
                    if MainGame.my_tank and MainGame.my_tank.live:
                        MainGame.my_tank.stop = False
                        if event.key == pygame.K_LEFT:
                            MainGame.my_tank.direction = "L"
                        elif event.key == pygame.K_RIGHT:
                            MainGame.my_tank.direction = "R"
                        elif event.key == pygame.K_UP:
                            MainGame.my_tank.direction = "U"
                        elif event.key == pygame.K_DOWN:
                            MainGame.my_tank.direction = "D"
                        elif event.key == pygame.K_SPACE:
                            MainGame.my_tank.stop = True
                            if len(MainGame.myBulletList) < MainGame.enemyTankCount:
                                my_bullet = Bullets(MainGame.my_tank)
                                MainGame.myBulletList.append(my_bullet)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        if MainGame.my_tank and MainGame.my_tank.live:
                            MainGame.my_tank.stop = True


    class Tank(BaseItem):
        def __init__(self, left, top):
            self.images = {"U": pygame.image.load("enemy_tank(up).png"),
                           "D": pygame.image.load("enemy_tank(down).png"),
                           "L": pygame.image.load("enemy_tank(left).png"),
                           "R": pygame.image.load("enemy_tank(right).png")}
            self.direction = "U"
            self.image = self.images[self.direction]
            self.rect = self.image.get_rect()
            self.rect.left = left
            self.rect.top = top
            self.speed = 10
            self.stop = True
            self.live = True
            self.old_left = self.rect.left
            self.old_top = self.rect.top

        def move(self):
            self.old_left = self.rect.left
            self.old_top = self.rect.top
            if self.direction == "L":
                if self.rect.left > 0:
                    self.rect.left -= self.speed
            elif self.direction == "U":
                if self.rect.top > 0:
                    self.rect.top -= self.speed
            elif self.direction == "D":
                if self.rect.top + self.rect.height < h:
                    self.rect.top += self.speed
            elif self.direction == "R":
                if self.rect.left + self.rect.height < w:
                    self.rect.left += self.speed

        def shot(self):
            num = random.randint(1, 10000)
            if num < (MainGame.level * 5):
                return Bullets(self)

        def stay(self):
            self.rect.left = self.old_left
            self.rect.top = self.old_top

        def hit_wall(self):
            for wall in MainGame.Wall1List:
                if pygame.sprite.collide_rect(self, wall):
                    self.stay()

        def display_tank(self):
            self.image = self.images[self.direction]
            """self.rect.x = random.randint(200, 400)
            self.rect.y = random.randint(200, 400)"""
            MainGame.window.blit(self.image, self.rect)


    class MyTank(Tank):
        def __init__(self, left, top):
            super(MyTank, self).__init__(left, top)

        def my_tank_and_enemy_tank_in_a_space(self):
            for enemyTank in MainGame.enemyTankList:
                if pygame.sprite.collide_rect(self, enemyTank):
                    self.stay()


    class EnemyTank(Tank):
        def __init__(self, left, top, speed):
            super(EnemyTank, self).__init__(left, top)
            self.images = {
                "U": pygame.image.load("tank(up).png"),
                "R": pygame.image.load("tank(right).png"),
                "D": pygame.image.load("tank(down).png"),
                "L": pygame.image.load("tank(left).png")
            }
            self.direction = self.rand_direction()
            self.image = self.images[self.direction]
            self.rect = self.image.get_rect()
            self.rect.left = left
            self.rect.top = top
            self.speed = speed
            self.flag = True
            self.step = random.randint(20, 60)

        def enemy_tank_and_my_tank_in_a_space(self):
            if pygame.sprite.collide_rect(self, MainGame.my_tank):
                self.stay()

        @staticmethod
        def rand_direction():
            num = random.randint(1, 4)
            if num == 1:
                return "U"
            elif num == 2:
                return "D"
            elif num == 3:
                return "L"
            elif num == 4:
                return "R"

        def rand_move(self):
            if self.step <= 0:
                self.direction = self.rand_direction()
                self.step = random.randint(20, 60)
            else:
                self.move()
                self.step -= 1


    class Bullets(BaseItem):
        def __init__(self, tank):
            self.image = pygame.image.load("子弹.png")
            self.direction = tank.direction
            self.rect = self.image.get_rect()
            if self.direction == "U":
                self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
                self.rect.top = self.rect.top = tank.rect.top - self.rect.height
            elif self.direction == "D":
                self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
                self.rect.top = tank.rect.top + tank.rect.height
            elif self.direction == "L":
                self.rect.left = tank.rect.left + self.rect.width / 2 - self.rect.width / 2
                self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
            elif self.direction == "R":
                self.rect.left = tank.rect.left + tank.rect.width
                self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
            self.speed = 5
            self.live = True

        def move(self):
            if self.direction == "U":
                if self.rect.top > 0:
                    self.rect.top -= self.speed
                else:
                    self.live = False
            elif self.direction == "R":
                if self.rect.left + self.rect.width < w:
                    self.rect.left += self.speed
                else:
                    self.live = False
            elif self.direction == "D":
                if self.rect.top + self.rect.height < h:
                    self.rect.top += self.speed
                else:
                    self.live = False
            elif self.direction == "L":
                if self.rect.left > 0:
                    self.rect.left -= self.speed
                else:
                    self.live = False

        def hit_wall(self):
            for wall in MainGame.Wall1List:
                if pygame.sprite.collide_rect(self, wall):
                    self.live = False
                    wall.hp -= 1
                    if wall.hp <= 0:
                        wall.live = False
                        Explode.display_explode(wall)

        def display_bullets(self):
            MainGame.window.blit(self.image, self.rect)

        def my_bullets_hit_enemy_tank(self):
            for enemyTank in MainGame.enemyTankList:
                if pygame.sprite.collide_rect(enemyTank, self):
                    enemyTank.live = False
                    self.live = False
                    explode = Explode(enemyTank)
                    MainGame.explode_list.append(explode)

        def enemy_bullets_hit_my_tank(self):
            if MainGame.my_tank and MainGame.my_tank.live:
                if pygame.sprite.collide_rect(MainGame.my_tank, self):
                    explode = Explode(MainGame.my_tank)
                    MainGame.explode_list.append(explode)
                    self.live = False
                    MainGame.my_tank.live = False

        def enemy_bullets_hit_enemy_tank(self):
            for enemyTank in MainGame.enemyTankList:
                if pygame.sprite.collide_rect(enemyTank, self):
                    enemyTank.live = False
                    self.live = False
                    explode = Explode(enemyTank)
                    MainGame.explode_list.append(explode)

        def bullet_hit_bullet(self):
            if self.live:
                for i in MainGame.enemyBulletList:
                    for j in MainGame.myBulletList:
                        if pygame.sprite.collide_rect(i, j):
                            explode = Explode(i)
                            MainGame.explode_list.append(explode)
                            explode = Explode(j)
                            MainGame.explode_list.append(explode)
                            i.live = False
                            j.live = False

    class Wall1:
        def __init__(self, left, top):
            self.image = pygame.image.load("墙壁.png")
            self.images = [pygame.image.load("爆炸效果.png")]
            self.rect = self.image.get_rect()
            self.rect.left = left
            self.rect.top = top
            self.step = 0
            self.live = True
            self.hp = 1


        def display_wall(self):
            MainGame.window.blit(self.image, self.rect)
    class Wall2:
        def __init__(self, left2, top2):
            self.image2 = pygame.image.load("wall.png")
            self.rect2 = self.image2.get_rect()
            self.rect2.left = left2
            self.rect.top = top2

        def display_wall2(self):
            MainGame.window.blit(self.image2, self.rect2)


    class Explode:
        def __init__(self, tank):
            self.rect = tank.rect
            self.images = [pygame.image.load("爆炸效果.png")]
            self.step = 0
            self.image = self.images[self.step]
            self.live = True


        def display_explode(self):
            if self.step < len(self.images):
                self.image = self.images[self.step]
                self.step += 1
                MainGame.window.blit(self.image,self.rect)
            else:
                self.live = False
                self.step = 0


    class Music:
        def __init__(self):
            pass

        def play(self):
            pass

except ValueError:
    pass
if __name__ == "__main__":
    MainGame().start_game()
