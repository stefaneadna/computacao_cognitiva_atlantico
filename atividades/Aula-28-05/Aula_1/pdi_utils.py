import matplotlib.pyplot as plt
import numpy as np


def load_red_roses():
    return plt.imread("/home/juliana/Área de Trabalho/github/computacao_cognitiva_atlantico/atividades/Aula-28-05/Aula_1/imgs/red_roses.png")

def load_page_image():
    return plt.imread("/home/juliana/Área de Trabalho/github/computacao_cognitiva_atlantico/atividades/Aula-28-05/Aula_1/imgs/page.jpg")

def load_chess_image():
    return plt.imread("/home/juliana/Área de Trabalho/github/computacao_cognitiva_atlantico/atividades/Aula-28-05/Aula_1/imgs/chess_gray.png")

def load_woman():
    return plt.imread("/home/juliana/Área de Trabalho/github/computacao_cognitiva_atlantico/atividades/Aula-28-05/Aula_1/imgs/woman.png")

def load_flipped_seville():
    return plt.imread("/home/juliana/Área de Trabalho/github/computacao_cognitiva_atlantico/atividades/Aula-28-05/Aula_1/imgs/flipped_seville.png")

def load_lena():
    return plt.imread("/home/juliana/Área de Trabalho/github/computacao_cognitiva_atlantico/atividades/Aula-28-05/Aula_1/imgs/lena.png")

def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

def manual_rgb2gray(rgb_img):
    return np.array((rgb_img[:,:,0]*0.29 + rgb_img[:,:,1]*0.59 + rgb_img[:,:,2]*0.11)).astype(int)
