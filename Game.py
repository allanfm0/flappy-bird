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

imagens_passaro = [
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
    imgs = imagens_passaro

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
        self.imagem = imgs[0]


class Cano:

    pass


class Chao:
    pass
