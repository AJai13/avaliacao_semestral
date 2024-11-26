from sistema_transporte.i_transporte import iTransporte


class transporte_aereo(iTransporte):
    def entregar(self, encomenda):
        if encomenda["peso"] > 20 or encomenda["dimensoes"] > (50, 50, 50):
            return f"\nEncomenda '{encomenda['descricao']}' não pode ser entregue via transporte aéreo devido às restrições de peso ou dimensão."
        return f"\nEntregar '{encomenda['descricao']}' via transporte aéreo."
