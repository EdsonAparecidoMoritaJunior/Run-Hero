import pygame
import sys


class StartScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.title_font = pygame.font.Font(None, 100)  # Larger font for the "Run Hero" title/ Fonte maior para o título "Run Hero"
        self.bg_image = pygame.image.load('assets/images/start_background.png')
        self.bg_image = pygame.transform.scale(self.bg_image, (500, 400))  # Resize to 500x400/ Redimensiona para 500x400

        # "START" button/ Botão "START"
        self.start_text = self.font.render('START', True, (255, 0, 0))  # Red color for START/ Cor Vermelha do START
        self.start_rect = self.start_text.get_rect(center=(250, 300))

        # "Run Hero" title at the top of the screen/ Título "Run Hero" na parte superior da tela
        self.title_text = self.title_font.render('Run Hero', True, (0, 255, 0))  # Light Green color/ Cor Verde Claro
        self.title_rect = self.title_text.get_rect(center=(250, 50))  # Position at the top of the screen/ Posiciona no topo da tela

    def show_start_screen(self):
        running = True
        while running:
            self.screen.blit(self.bg_image, (0, 0))  # Background of the start screen/ Fundo da tela inicial
            self.screen.blit(self.title_text, self.title_rect)  # Display "Run Hero" title/ Exibe o título "Run Hero"
            self.screen.blit(self.start_text, self.start_rect)  # Display the "START" button/ Exibe o texto "START"
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(event.pos):
                        return True  # Return True when the click is detected/ Retorna True quando o clique é detectado
            pygame.time.delay(10)  # Small delay to avoid excessive CPU consumption/ Pequeno atraso para evitar consumo excessivo de CPU

        return False  # If no click, the loop continues/ Se não clicar, o loop continuará
