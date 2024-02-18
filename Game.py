import pygame
import os
import random

tela_largua = 500
tela_altura = 800

imagem_cano = pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "pipe.png")))
imagen_chao = pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "base.png")))
imagem_background = pygame.transform.scale2x(
    pygame.image.load(os.path.join("imgs", "bg.png")))

IMAGEMS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(
        os.path.join("imgs", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join("imgs", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join("imgs", "bird3.png")))

]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


class Passaro:
    IMGS = IMAGEMS_PASSARO

    # animaçoes da rotacao
    rotacao_maxima = 25
    velocidade_rotacao = 20
    tempo_animacao = 5

    # atributos do passaro
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo ** 2) + self.velocidade * self.tempo

        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.altura < self.rotacao_maxima:
                self.altura = self.rotacao_maxima
        else:
            if self.angulo > -90:
                self.angulo = self.velocidade_rotacao


class Cano:

    pass


class Chao:
    pass
