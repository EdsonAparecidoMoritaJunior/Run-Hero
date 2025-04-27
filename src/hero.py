import pygame

class Hero:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/images/hero.png').convert()
        self.image.set_colorkey((255, 255, 255))  # Define o branco da imagem como transparente
        self.image = pygame.transform.scale(self.image, (40, 40))  # Ajustar o tamanho do herói
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = 5

    def update(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:  # Impede o herói de sair pela esquerda
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < 500:  # Impede o herói de sair pela direita
            self.rect.x += self.velocity

        screen.blit(self.image, self.rect)
