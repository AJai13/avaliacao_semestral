from sistema_transporte.i_transporte import iTransporte


class transporte_terrestre(iTransporte):
    def __init__(self, transportadora_local):
        self.transportadora_local = transportadora_local

    def entregar(self, encomenda):
        if not self.transportadora_local:
            return "\nErro: Nenhuma transportadora local foi selecionada para transporte terrestre."
        return f"\nEntregar '{encomenda['descricao']}' via transporte terrestre."
