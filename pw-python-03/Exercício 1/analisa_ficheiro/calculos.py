def calcula_linhas(file):
    with open(file) as f:
        line = f.readlines()
        return len(line)


def calcula_carateres(file):
    with open(file) as f:
        char = f.read().replace("\n", "").replace(" ", "")
        return len(char)


def calcula_palavra_comprida(file):
    with open(file) as f:
        word = f.read().split()
        wordL = sorted(word, key=len)
        return wordL[-1]


def calcula_ocorrencia_de_letras(file):
    with open(file) as f:
        char = f.read()
        count = dict()

        for palavra in char.split():
            for letra in palavra.lower():
                count[letra] = count.get(letra, 0)+1
        return char

