from sistema_transporte.i_transporte import iTransporte


class transporte_drones(iTransporte):
    def entregar(self, encomenda):
        if encomenda["local"] not in ["área metropolitana"]:
            return "\nEntrega por drones disponível apenas em áreas metropolitanas."
        if encomenda["peso"] > 5:
            return "\nEntrega por drones disponível apenas para pacotes leves."
        return f"\nEntregar '{encomenda['descricao']}' via drones."
