import automovel as a


def main():
    """"Testes disponibilizados no enunciado"""
    a1 = a.automovel(60, 10, 15)
    print(a1.autonomia())
    print(a1.abastece(45))
    print(a1.percorre(150))
    print(a1.percorre(250))
    print(a1.quant_comb)


if __name__ == "__main__":
    main()
