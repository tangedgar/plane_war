import pygame
import time
import random
from pygame.locals import *


class Plane(object):
    def __init__(self, screen, plane_name):
        self.plane_name = plane_name
        self.screen = screen
        self.image = pygame.image.load(self.image_name).convert()
        self.bullet_list = []
        self.rect = self.image.get_rect()

    def rect(self):
        return self.rect

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.rect[0] = self.x
        self.rect[1] = self.y
        need_del_bullet = []
        for item in self.bullet_list:
            if item.judge():
                need_del_bullet.append(item)
        for del_item in need_del_bullet:
            self.bullet_list.remove(del_item)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    # 英雄飞机的活动范围
    def move_left(self):
        if self.x > -40:
            self.x -= 20
        else:
            self.x += 20

    def move_right(self):
        if self.x < 480 - 60:
            self.x += 20
        else:
            self.x -= 20

    def move_up(self):
        if self.y > 400:
            self.y -= 20
        else:
            self.y += 20

    def move_down(self):
        if self.y < 620:
            self.y += 20
        else:
            self.y -= 20


# 定义公共子弹类
class PublicBullet(object):
    def __init__(self, x, y, screen, plane_name):
        self.screen = screen
        self.plane_name = plane_name
        if self.plane_name == "hero":
            self.x = x + 40
            self.y = y - 30
            image_name = "./feiji/bullet-3.gif"
        elif self.plane_name == "enemy":
            self.x = x + 30
            self.y = y + 30
            image_name = "./feiji/bullet-1.gif"
        self.image = pygame.image.load(image_name).convert()
        self.rect = self.image.get_rect()

    def rect(self):
        return self.rect

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.rect[0] = self.x
        self.rect[1] = self.y

    def move(self):
        if self.plane_name == "hero":
            self.y -= 30
        elif self.plane_name == "enemy":
            self.y += 10

    def judge(self):
        if self.y > 750 or self.y < 0:
            return True
        else:
            return False


# 作为飞机类的子类，我方飞机类仅需要在属性值做一些初始化
class HeroPlane(Plane):
    def __init__(self, screen, plane_name):
        self.x = 0
        self.y = 600
        self.image_name = "./feiji/hero.gif"
        # 调用父类的构造函数完成初始化设置
        super().__init__(screen, plane_name)

    # 发射子弹的方法
    def launch_bullet(self):
        new_bullet = PublicBullet(self.x, self.y, self.screen, self.plane_name)
        self.bullet_list.append(new_bullet)

    def reset(self):
        # 飞机被击中后重设开始位置
        self.x = 200
        self.y = 600


# 作为飞机类的子类，敌方飞机类需要在属性值上做一些初始化，并重写发射子弹的方法
class EnemyPlane(Plane):
    def __init__(self, screen, plane_name):
        self.x = 230
        self.y = 50

        self.image_name = "./feiji/enemy-1.gif"

        super().__init__(screen, plane_name)

        self.direction = "right"

    def launch_bullet(self):
        number = random.randint(30, 100)
        if number == 88:
            new_bullet = PublicBullet(self.x, self.y, self.screen, self.plane_name)
            self.bullet_list.append(new_bullet)

    # 敌方飞机自有方法
    def move(self):
        if self.direction == "right":
            self.x += 10
        elif self.direction == "left":
            self.x -= 10
        elif self.direction == "up":
            self.y -= 10
        elif self.direction == "down":
            self.y += 10
        if self.x > 480 - 55:
            self.direction = "down"
            if self.y > 200:
                self.direction = "left"
        if self.x < 0:
            self.direction = "up"
            if self.y < 5:
                self.direction = "right"

    def reset(self):

        # 飞机被击中后重设开始位置
        self.x = random.randint(100, 380)
        self.y = random.randint(0, 230)


def start():  # 开始游戏
    # 1 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((690, 720), 0, 32)

    # 2 创建一个和窗口大小相同的图片，用来充当背景
    image_file_path = './feiji/background.png'
    background = pygame.image.load(image_file_path).convert()

    image_file_path = './feiji/description.png'
    description = pygame.image.load(image_file_path)

    image_file_path = './feiji/score_hp.png'
    score_hp = pygame.image.load(image_file_path)

    image_file_path = './feiji/boss_HP.png'
    boss_HP = pygame.image.load(image_file_path)

    image_file_path = './feiji/line.png'
    line = pygame.image.load(image_file_path)

    image_file_path = './feiji/max_score.png'
    max_score = pygame.image.load(image_file_path)

    image_file_path = './feiji/button_nor.png'
    button_nor = pygame.image.load(image_file_path)
    image_file_path = './feiji/button_p.png'
    button_p = pygame.image.load(image_file_path)

    image_file_path = './feiji/restart_sel.png'
    restart_sel = pygame.image.load(image_file_path)
    image_file_path = './feiji/quit_sel.png'
    quit_sel = pygame.image.load(image_file_path)

    # 3 创建一个飞机对象和敌人飞机
    hero_plane = HeroPlane(screen, "hero")
    enemy_plane = EnemyPlane(screen, "enemy")

    # 4 把背景图片放到窗口中显示
    while True:
        screen.blit(background, (0, 0))
        screen.blit(description, (480, 290))
        screen.blit(score_hp, (480, 180))
        screen.blit(boss_HP, (480, 140))
        screen.blit(line, (480, 280))
        screen.blit(max_score, (480, 100))
        screen.blit(button_nor, (480, 0))
        screen.blit(button_p, (480, 48))
        screen.blit(restart_sel, (480, 5))
        screen.blit(quit_sel, (483, 55))
        hero_plane.display()
        enemy_plane.display()
        enemy_plane.move()
        enemy_plane.launch_bullet()

        for bullet in hero_plane.bullet_list:
            if pygame.Rect.colliderect(enemy_plane.rect, bullet.rect):
                enemy_plane.reset()
                break

        for bullet in enemy_plane.bullet_list:
            if pygame.Rect.colliderect(hero_plane.rect, bullet.rect):
                hero_plane.reset()
                break

        # 判断用户是否点击了相应按键
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    hero_plane.move_left()
                elif event.key == K_d or event.key == K_RIGHT:
                    hero_plane.move_right()
                elif event.key == K_w or event.key == K_UP:
                    hero_plane.move_up()
                elif event.key == K_s or event.key == K_DOWN:
                    hero_plane.move_down()
                elif event.key == K_SPACE:
                    hero_plane.launch_bullet()
        bools = pygame.key.get_pressed()
        if bools[pygame.K_UP] == 1:
            hero_plane.move_up()
        if bools[pygame.K_DOWN] == 1:
            hero_plane.move_down()
        if bools[pygame.K_LEFT] == 1:
            hero_plane.move_left()
        if bools[pygame.K_RIGHT] == 1:
            hero_plane.move_right()
        time.sleep(0.05)
        pygame.display.update()


if __name__ == '__main__':
    start()
