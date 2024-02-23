import pyautogui as ag
from time import sleep
import keyboard
import sys

def ATQ():
    press_tecla('1', 1.7)


def verificar_imagem(img):
    while True:
        try:
            posicao = ag.locateOnScreen(img)
            if posicao is not None:
                print(f'Imagem encontrada nas coordenadas {posicao}')
                ATQ()
            else:
                print('Imagem não encontrada.')
                movimento_circular()
        except ag.ImageNotFoundException:
            print('Erro: Imagem não encontrada.')
            movimento_circular()

def press_tecla(tecla, temp):
    keyboard.press(tecla)
    keyboard.release(tecla)
    sleep(temp)
    print(tecla)


def movimento_circular():
    press_tecla('w', 0.5)
    press_tecla('d', 0.5) 
    press_tecla('s', 0.5) 
    press_tecla('a', 0.5)  


sleep(2)
print('Iniciou')
#ag.click(718,184, duration=1)
verificar_imagem(r'img\img01.png')