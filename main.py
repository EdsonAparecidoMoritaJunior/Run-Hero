import pygame
from src.startscreen import StartScreen
from src.Game import Game

def main():
    pygame.init()

    # Tamanho da tela
    screen_width = 500  # Ajuste para a largura desejada
    screen_height = 400  # Ajuste para a altura desejada
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Run Hero')

    # Tela inicial
    start_screen = StartScreen(screen)

    # Ao clicar "start", o jogo começa
    if start_screen.show_start_screen():
        game = Game(screen)
        game.run()

if __name__ == "__main__":
    main()

