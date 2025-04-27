import pygame
import random

class Platform:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/images/platform.png')
        self.image = pygame.transform.scale(self.image, (60, 10))  # Ajustar o tamanho da plataforma
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 1  # Velocidade de queda

    def update(self, screen):
        self.rect.y += self.velocity
        if self.rect.y > 400:  # Se a plataforma descer para fora da tela, ela reaparece no topo
            self.rect.y = random.randint(-50, -10)
            self.rect.x = random.randint(0, 500 - self.rect.width)  # Garante que a plataforma caia em posições aleatórias

        screen.blit(self.image, self.rect)
