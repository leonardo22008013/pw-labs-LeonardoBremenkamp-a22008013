def pede_pasta() -> "Retorna o nome de uma pasta se existir" :
    import os
    while True:
        folder = input("Entre com o nome da pasta:")

        if os.path.isdir(folder):
            return os.path.basename(folder)


def calcula_tamanho_pasta(folder: 'É um ficheiro pasta') -> "Função retorna tamanho de uma pasta":
    import os
    total = 0
    lista_ficheiros = os.listdir(folder)
    for file in lista_ficheiros:
        caminho = os.path.join(folder, file)
        if os.path.isfile(caminho):
            total += os.path.getsize(caminho)
        elif os.path.isdir(caminho):
            total += calcula_tamanho_pasta(caminho)
    return total
