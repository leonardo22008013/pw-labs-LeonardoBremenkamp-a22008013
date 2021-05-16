from os import path


def pede_nome():
    while True:
        file = input("Entre com o nome do ficheiro: ")

        if path.exists(f"{file}.txt"):
            print(f"O fichei {file}.txt existe")
            return file


def gera_nome(file):
    return file.replace('.txt', '.json')
