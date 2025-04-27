import pygame
from src.startscreen import StartScreen
from src.Game import Game

def main():
    pygame.init()

    # Screen Size/Tamanho da tela
    screen_width = 500  # Adjust do desired width/ Ajuste para a largura desejada
    screen_height = 400  # Adjust to desired height/ Ajuste para a altura desejada
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Run Hero')

    # Start Screen/ Tela inicial
    start_screen = StartScreen(screen)

    # When 'start' is clicked, the game begins/ Ao clicar "start", o jogo começa
    if start_screen.show_start_screen():
        game = Game(screen)
        game.run()

if __name__ == "__main__":
    main()

