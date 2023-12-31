import pygame
import os

class Buff:
    buffs_wave = []
    wave_length = 2

    speed_increment = 0

    # dictionary of buffs and their images
    BUFFSIMGS = {
        "atackspeed" : pygame.transform.scale(pygame.image.load(os.path.join("assets", "tinywow_axe_42166769.png")), (20,20)),
        "fasterBullets" : pygame.image.load(os.path.join("assets", "Critical_strike_chance_icon.png")),
        "speed" : pygame.image.load(os.path.join("assets", "tinywow_Movement_speed_icon_42171369.png")),
        "moreLives" : pygame.transform.scale(pygame.image.load(os.path.join("assets", "heart.png")), (20,20)),
        "piercingBullets" : pygame.image.load(os.path.join("assets", "Armor_penetration_icon.png")),
        "shield" : pygame.image.load(os.path.join("assets", "pixel_laser_red.png")),
        "laser" : pygame.image.load(os.path.join("assets", "pixel_laser_red.png")),		
    }

    buff_Timer = {
        "atackspeed" : 0,
        "fasterBullets" : 0,
        "speed" : 0,
        "moreLives" : 0,
        "piercingBullets" : 0,
        "shield" : 0,
        "laser" : 0,		
    }

    def __init__(self, x, y, type):
        self.x = x
        self.y = y

        self.type = type
        self.img = self.BUFFSIMGS[type]
        self.mask = pygame.mask.from_surface(self.img)

        self.speed = 1.5 + self.speed_increment

    # draw the buffs
    def draw(self, window):
        window.blit(self.img, (self.x, self.y)) # draw the ship

    # move the buffs
    def move(self):
        self.y += self.speed

    def run_timer(self):
        if self.buff_Timer[self.type] > 0:
            self.buff_Timer[self.type] -= 1
    
    # return the width of the object
    def get_width(self):
        return self.img.get_width()

    # return the height of the object
    def get_height(self):
        return self.img.get_height()
#.