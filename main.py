import sys, time
import pygame
from pygame import mixer

from sprites import *


pygame.init()
mixer.init()


WIDTH, HEIGHT = 638, 482
WINDOW_TITLE = "PONG"

BACKGROUND_COLOR = (0, 0, 0)

FPS = 60


# load assets

tab_changing_sound = mixer.Sound('assets/Sounds/changing-tab.wav')
jumping_sound = mixer.Sound('assets/Sounds/jumping.wav')
loosing_sound = mixer.Sound('assets/Sounds/loosing.wav')
pop_sound = mixer.Sound('assets/Sounds/pop.wav')



font_bigger = pygame.font.Font('fonts\ARCADE.ttf', 52)
font = pygame.font.Font('fonts\ARCADE.ttf', 32)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
pygame.display.flip()

clock = pygame.time.Clock()




running = True


def prepare(screen):
    screen.fill(BACKGROUND_COLOR)



def title_screen():
    global running, font, font_bigger
    break_loop = False

    text_title = font_bigger.render('PONG', True, (255, 255, 255))
    textRectTitle = text_title.get_rect()
    textRectTitle.center = (WIDTH // 2, HEIGHT // 5)

    text_keypress = font.render('press any key to play', True, (128, 128, 128))
    textRectKeypress = text_keypress.get_rect()
    textRectKeypress.center = (WIDTH // 2, HEIGHT // 3.2)



    while running:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                break_loop = True
        
        if break_loop:
            break
        

        prepare(screen)
        clock.tick(FPS)

        
        screen.blit(text_title, textRectTitle)
        screen.blit(text_keypress, textRectKeypress)

        pygame.display.flip()





def game():
    global running, font, font_bigger, loosing_sound, jumping_sound, pop_sound

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    player = Player(screen)
    ball = Ball(screen)

    score = 0
    gameover = False

    # Show when game is over
    show_gameover_text = True
    gameover_text_c = 0


    while running:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            
            keys = pygame.key.get_pressed()


            if keys[pygame.K_w]:
                player.move_up()
            if keys[pygame.K_s]:
                player.move_down()


        prepare(screen)
        clock.tick(FPS)

        if not gameover:
            player.draw()

            if player.has_colide(ball.sprite):
                score += 1
                ball.colision()
                jumping_sound.play()
            ball.draw()
            if ball.reached_border:
                pop_sound.play()
            gameover = ball.gameover
            if gameover:
                loosing_sound.play()

        else:
            # if game is over
            text_gameover = font_bigger.render('GAME OVER', True, (255, 0, 0))
            textRectGameover = text_gameover.get_rect()
            textRectGameover.center = (WIDTH // 2, HEIGHT // 2)

            gameover_text_c += 1

            if gameover_text_c % int(FPS*0.5) == 0:
                if show_gameover_text:
                    show_gameover_text = False
                else:
                    show_gameover_text = True

            if show_gameover_text:
                screen.blit(text_gameover, textRectGameover)
            
            if gameover_text_c % (int(FPS*0.5) * 5) == 0:
                break
            

        text_title = font.render('PONG', True, (255, 255, 255))
        text_score = font.render(f'SCORE: {score}', True, (255, 255, 255))
        # create a rectangular object for the
        # text surface object
        textRectTitle = text_title.get_rect()
        textRectScore = text_score.get_rect()
        
        # set the center of the rectangular object.
        textRectTitle.center = (WIDTH // 2, 20)
        textRectScore.center = (WIDTH // 2, 40)

        screen.blit(text_title, textRectTitle)
        screen.blit(text_score, textRectScore)
        

        pygame.display.flip()
    

def main():
    global running, tab_changing_sound
    running = True


    while running:
        # show title screen
        print("[main] title_screen()")
        
        title_screen()
        tab_changing_sound.play()

        # start game if title screen exited
        print("[main] game()")
        game()
        tab_changing_sound.play()
        # show the title screen again after player lose the game


    raise RuntimeError("User quited session.")





if __name__ == "__main__":
    proc = main()
    pygame.quit()
    sys.exit(proc)