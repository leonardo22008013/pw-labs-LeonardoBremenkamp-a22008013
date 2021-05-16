class automovel:
    def __init__(self, cap_dep, quant_comb, consumo: 'instancia classe automovel') -> 'classe automóvel':
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo

    def combustivel(self: 'parametro inteiro') -> 'retorna quantidade':
        return int(self.quant_comb)

    def autonomia(self: 'parametro inteiro') -> 'retorna consumo a cada 100km':
        return int(self.quant_comb / (self.consumo / 100))

    def abastece(self, n_litros: 'parametro inteiro') -> 'retorna autonomia':
        if self.quant_comb + n_litros < self.cap_dep:
            self.quant_comb += n_litros
            return int(self.autonomia())
        return -1

    def percorre(self, n_km):
        return int(self.autonomia() - n_km)
