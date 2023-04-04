import pygame
import os
import sys

WIDTH,HEIGHT = 1550,800;
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MONOPOLY")

def background_0():
    bg_img = pygame.image.load(os.path.join('assets','bg.jpg'))
    bg_img = pygame.transform.scale(bg_img,(1550,800))


    WIN.blit(bg_img,(0,0))
    pygame.display.update()

FPS = 60;

def play_Button():
    pygame.init();
    screen = pygame.display.set_mode((1550,800))
    color_light = (241, 229, 172)
    color_dark = (255, 215, 0)
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel',35)
    text = smallfont.render('Play!' , True , (0,0,0))
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                    screen.fill((60,25,60))
        mouse = pygame.mouse.get_pos()
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.draw.rect(screen,color_light,[width/2,height/2,140,40])
            
        else:
            pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40])
        
        screen.blit(text , (width/2+50,height/2))
        pygame.display.update()


def main():
    clock =pygame.time.Clock()
    run = True
    while run:
        background_0();
        play_Button()
        clock.tick(FPS);
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
        
    pygame.quit()

if __name__ == "__main__":
    main()


