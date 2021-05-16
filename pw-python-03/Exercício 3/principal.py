from analisa_pasta import funcoes


def main():
    """ Para efeito de testes utilizar o nome analisa_pasta após execução do main"""
    print(funcoes.pede_pasta())
    print(funcoes.calcula_tamanho_pasta(funcoes.pede_pasta()))


if __name__ == '__main__':
    main()
