import pygame
pygame.init()

width=700
height=500
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("tumatalbog na platform game")


class Platform(object):
    def __init__(self, x, y, platform_width, platform_height):
        self. x=x
        self.y=y
        self.platform_width=platform_width
        self.platform_height=platform_height
        self.platform_velocity=10
        self.right=True
        self.left=False

        self.rect = pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.platform_width, self.platform_height))

        while self.right:
            self.x+=self.platform_velocity
            if self.rect.right==width:
                self.right=False
                self.left=True
            else:
                self.x-=self.platform_velocity
                if self.rect.left<=0:
                    self.right=True








p1=Platform(250, 100, 200, 20)
p2=Platform(250, 400, 200, 20)





run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False


    pygame.display.update()

pygame.quit()

