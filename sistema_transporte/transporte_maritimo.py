from sistema_transporte.i_transporte import iTransporte


class transporte_maritimo(iTransporte):
    def entregar(self, encomenda):
        if encomenda["destino"] != "internacional":
            return "\nErro: Transporte marítimo só está disponível para entregas internacionais."
        return f"\nEntregar '{encomenda['descricao']}' via transporte marítimo."
