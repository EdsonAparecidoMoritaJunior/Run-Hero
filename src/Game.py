import pygame
import random
from src.hero import Hero
from src.platform import Platform
from src.startscreen import StartScreen  # Importa a tela inicial

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.hero = Hero(250, 300)  # Posição inicial do herói
        self.platforms = [Platform(random.randint(100, 700), random.randint(100, 500)) for _ in range(10)]
        self.bg_image = pygame.image.load('assets/images/fase1_background.png')

        # Plataforma fixa no chão
        self.ground = pygame.image.load('assets/images/platform.png')
        self.ground = pygame.transform.scale(self.ground, (560, 20))  # Plataforma cobrindo toda a largura da tela
        self.ground_rect = self.ground.get_rect(topleft=(-35, 320))  # Posição na parte inferior

        self.start_time = pygame.time.get_ticks()  # Armazena o tempo de início do jogo

    def run(self):
        running = True
        while running:
            self.screen.blit(self.bg_image, (0, 0))  # Fundo do jogo

            # Desenha a plataforma fixa no chão
            self.screen.blit(self.ground, self.ground_rect)

            # Atualiza o herói e as plataformas
            self.hero.update(self.screen)
            for platform in self.platforms:
                platform.update(self.screen)

            # Checa se o herói colidiu com alguma plataforma
            if self.check_collision():
                self.game_over()

            # Exibe o tempo de sobrevivência
            self.show_time()

            # Verifica se o tempo de sobrevivência atingiu 30 segundos
            if pygame.time.get_ticks() - self.start_time >= 30000:  # 30 segundos
                self.level_cleared()

            pygame.display.flip()
            self.clock.tick(60)

            # Verifica os eventos de saída do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def check_collision(self):
        # Verifica se o herói colidiu com alguma plataforma
        for platform in self.platforms:
            if self.hero.rect.colliderect(platform.rect):
                return True
        return False

    def game_over(self):
        # Exibe a tela de Game Over e volta ao menu de start
        self.display_message("Game Over - Tente Novamente")
        pygame.display.flip()  # Atualiza a tela para mostrar a mensagem
        pygame.time.wait(2000)  # Pausa de 2 segundos antes de reiniciar o jogo
        self.wait_for_restart()

    def level_cleared(self):
        # Exibe a mensagem de vitória e volta ao menu de start
        self.display_message("Fase 1 Cleared!")
        pygame.display.flip()  # Atualiza a tela para mostrar a mensagem
        pygame.time.wait(2000)  # Pausa de 2 segundos antes de reiniciar o jogo
        self.wait_for_restart()

    def display_message(self, message):
        # Exibe a mensagem no centro da tela
        font = pygame.font.Font(None, 35)
        text = font.render(message, True, (255, 0, 0))  # Cor vermelha
        rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, rect)

    def show_time(self):
        # Exibe o tempo de sobrevivência
        time_survived = (pygame.time.get_ticks() - self.start_time) // 1000  # Convertendo para segundos
        font = pygame.font.Font(None, 36)
        text = font.render(f"Tempo de sobrevivência: {time_survived}s", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

    def wait_for_restart(self):
        # Aguarda o jogador clicar para reiniciar o jogo
        start_screen = StartScreen(self.screen)  # Instancia a tela inicial
        start_screen.show_start_screen()  # Exibe a tela inicial de start
        self.__init__(self.screen)  # Reinicia o jogo (reseta todas as variáveis)
