import pygame
from pygame.locals import *
import numpy as np
from sys import exit
import os
import cmath

pygame.init()

largura_janela, altura_janela = 700, 700
repetições = 500
Zoom = 1.5
cor = True
FPS = 5

rede = np.zeros((largura_janela, altura_janela,2))
tela = pygame.display.set_mode((largura_janela, altura_janela))
clock = pygame.time.Clock()

def atualizar():
    for col in range(largura_janela):
        for row in range(altura_janela):
            pontox = (col+0-largura_janela/Zoom)/(largura_janela/(Zoom*2)) #800 e 3000 para zoom 0.2,dividir por 2 90000 e 150 para zoom 0.001
            pontoy = (row+120-altura_janela/Zoom)/(altura_janela/(Zoom*2))   #/2 -4400,-7600 zoom 0.03 ,/2 -1308900,-2309200 zoom 0.0001
            if pontoy < 0:
                neg = -1
            else:
                neg = 1
            ponto = pontox + (cmath.sqrt(-(pontoy**2)))*neg
            Z = 0
            for i in range(repetições):
                Z = Z*Z +ponto                            #novos fraquetais: raiz quadrada de Z**4,  Z**Z
                if abs(Z) > 2:
                    rede[col][row][1] = i
                    break
            if abs(Z) < 2:
                rede[col][row][0] = 1
            else:
                rede[col][row][0] = 0

def desenhar(tela):
    tela.fill((255,255,255))
    for col in range(largura_janela):
        for row in range(altura_janela):
            if rede[col][row][0] == 1:
                tela.set_at((col,row),(0,0,0))
            elif cor:
                tela.set_at((col,row),(min(rede[col][row][1]*3,250),0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                repetições += 2
            if event.key == K_s:
                repetições -= 2
    atualizar()                
    desenhar(tela)
    clock.tick(FPS)
    pygame.display.flip()