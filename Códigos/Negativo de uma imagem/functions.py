import PIL
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
from imagens import FOTO_PNG, FOTO_PGM
"""
Os arquivos PGM armazenam imagens em tons de cinza.
Cada pixel na imagem contém só um ou dois bytes de informação.
Os arquivos PGM conseguem aramzenar diversos tons de cinza em uma imagem.
"""


def read_pgm(caminho_arquivo_pgm):
    """
    Lê um arquivo de imagem PGM e retorna os dados da imagem como uma lista (ASCII) ou um array NumPy (binário).

    Args:
        caminho_arquivo_pgm (str): Caminho para o arquivo de imagem PGM.

    Returns:
        list ou numpy.ndarray: Os dados da imagem como uma lista 2D (ASCII) ou array NumPy (binário).

    Raises:
        ValueError: Se o formato do arquivo PGM não for suportado (P2 ou P5) ou a profundidade de cor não for suportada (> 255).
    """

    with open(caminho_arquivo_pgm, 'rb') as f:
        # Lê o número mágico (P2 ou P5)
        magic_number = f.readline().strip()
        if magic_number == b'P2':
            ascii_format = True
            print("Lendo formato PGM ASCII...")
        elif magic_number == b'P5':
            ascii_format = False
            print("Lendo formato PGM binário...")
        else:
            raise ValueError("Formato de arquivo PGM não suportado (Apenas P2 ou P5)")

        # Ignora comentários (linhas iniciando com '#')
        line = f.readline()
        while line[0:1] == b'#':
            line = f.readline()

        # Lê largura, altura e profundidade de cor
        largura, altura = map(int, line.split())
        profundidade = int(f.readline())

        if profundidade > 255:
            raise ValueError("Profundidade de cor não suportada (Profundidade máxima 255)")

        # Lê dados da imagem baseado no formato
        if ascii_format:
            img = []
            for _ in range(altura):
                linha = [int(val) for val in f.readline().split()]
                img.append(linha)
        else:
            img = np.fromfile(f, dtype=np.uint8, count=largura*altura).reshape(altura, largura)

    return img


def abrir_pgm_com_matplotlib(caminho_arquivo_pgm):
    """
    Abre uma imagem PGM usando o Matplotlib.

    Args:
        caminho_arquivo_pgm (str): Caminho para o arquivo de imagem PGM.

    Returns:
        list ou numpy.ndarray: Os dados da imagem como uma lista 2D (ASCII) ou array NumPy (binário).

    Raises:
        ValueError: Se o formato do arquivo PGM não for suportado (P2 ou P5) ou a profundidade de cor não for suportada (> 255).
    """

    img = read_pgm(caminho_arquivo_pgm)

    # Exibe a imagem usando o Matplotlib
    plt.imshow(img, cmap='gray')
    plt.title(f"Imagem PGM: {caminho_arquivo_pgm}")
    plt.show()

    return img


def imgalloc(nl, nc):
    """
    Alocar memória e cria uma imagem vazia.

    Args:
        nl (int): Número de linhas da imagem.
        nc (int): Número de colunas da imagem.

    Returns:
        list: Uma lista 2D representando a imagem com zeros em cada pixel.
    """

    img = []

    # Laço para linhas
    for i in range(nl):
        lin = []

        # Laço para colunas
        for j in range(nc):
            lin.append(0)  # Inicializa cada pixel com 0 (valor padrão)

        img.append(lin)  # Adiciona a linha criada à imagem

    return img


def calculo_do_negativo(imagem):
    """
    Calcula o negativo de uma imagem.

    Args:
        imagem (list): Uma lista 2D representando a imagem original.

    Returns:
        list: Uma lista 2D representando a imagem negativa.
    """

    nl = len(imagem)  # Número de linhas da imagem
    nc = len(imagem[0])  # Número de colunas da imagem

    # Alocar memória e criar imagem vazia
    imgs = imgalloc(nl, nc)

    # Percorrer cada pixel da imagem
    for i in range(nl):
        for j in range(nc):
            # Calcular o valor negativo do pixel
            imgs[i][j] = 255 - imagem[i][j]

    # Exibir a imagem negativa
    plt.imshow(imgs, cmap='gray')
    plt.title("Imagem Negativa")
    plt.show()

    return imgs


def calculo_simples_do_negativo(imagem):
    """
    Calcula o negativo de uma imagem usando o NumPy.

    Args:
        imagem (list): Uma lista 2D representando a imagem original.

    Returns:
        None: Exibe a imagem negativa, mas não retorna nenhum valor.
    """

    # Converte a imagem para um array NumPy
    imgT = np.asarray(imagem)

    # Calcula o negativo da imagem (255 - valor original)
    imgT = 255 - imgT

    # Exibe a imagem negativa
    plt.imshow(imgT, cmap='gray')
    plt.title("Imagem Negativa (NumPy)")
    plt.show()

    return None


"""
Lidando agora com PIL
Algumas informações:
.format -> formato da imagem
.size -> tamanho da imagem
.mode -> modo da imagem
"""


def abrindo_com_pil(imagem):
    """
    Abre uma imagem usando a biblioteca PIL.

    Args:
        imagem (str): Caminho para o arquivo de imagem.

    Returns:
        None: Exibe a imagem usando o Matplotlib.
    """

    # Abre a imagem com a biblioteca PIL
    img = Image.open(imagem)

    print(f'Lendo formato: {img.format}')

    # Exibe a imagem usando o Matplotlib
    plt.imshow(img)
    plt.title(f"Imagem: {imagem}")
    plt.show()

    return None


def convertendo_imagem_para_arrays_numpy(imagem):
    """
    Converte uma imagem para um array NumPy.

    Args:
        imagem (str): Caminho para o arquivo de imagem.

    Returns:
        None: Exibe a imagem usando o Matplotlib.
    """

    # Lê a imagem como um array NumPy
    data = img.imread(imagem)

    # Exibe a imagem usando o Matplotlib
    plt.imshow(data)
    plt.title(f"Imagem como Array NumPy: {imagem}")
    plt.show()

    return None


def menu():
    print('1 - Abrir uma imagem PGM')
    print('2 - Abrir uma imagem com PIL')
    print('3 - Calcular o negativo de uma imagem PGM')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        abrir_pgm_com_matplotlib(FOTO_PGM)

    elif opcao == 2:
        abrindo_com_pil(FOTO_PNG)

    elif opcao == 3:
        print('1 - Usando numpy')
        print('2 - Usando Alocação de memória')
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            img = read_pgm(FOTO_PGM)
            calculo_simples_do_negativo(img)
        elif opcao == 2:
            img = read_pgm(FOTO_PGM)
            calculo_do_negativo(img)
    else:
        print('Opção inválida')
