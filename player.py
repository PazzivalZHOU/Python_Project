import pygame

class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        

    def draw(self, screen, x, y, color=(200, 200, 200)):
        self.rect.topleft = (x, y)
        
        if self.image:
            # 调用图片
            screen.blit(self.image, self.rect)
        else:
            # 如果 image 为 None，则通过函数直接绘制一个矩形
            pygame.draw.rect(screen, color, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)