from sistema_transporte.i_transporte import iTransporte
from sistema_transporte.transporte_aereo import transporte_aereo
from sistema_transporte.transporte_drones import transporte_drones
from sistema_transporte.transporte_maritimo import transporte_maritimo
from sistema_transporte.transporte_terrestre import transporte_terrestre


class sistema_de_transporte:
    def __init__(self):
        self.transporte = None

    def set_transporte(self, transporte: iTransporte):
        self.transporte = transporte

    def entregar(self, encomenda):
        if not self.transporte:
            return "Nenhum tipo de transporte selecionado."
        return self.transporte.entregar(encomenda)

    def selecionar_transporte(self, encomenda):
        if encomenda["local"] == "área metropolitana" and encomenda["peso"] <= 5:
            # Prioriza drones para entregas leves em áreas metropolitanas
            self.transporte = transporte_drones()
        elif encomenda["destino"] == "internacional":
            # Transporte marítimo para entregas internacionais
            self.transporte = transporte_maritimo()
        elif encomenda["peso"] > 20 or encomenda["dimensoes"] > (50, 50, 50):
            # Transporte terrestre para pacotes grandes ou pesados
            self.transporte = transporte_terrestre(transportadora_local="Transportadora Narcos")
        else:
            # Transporte aéreo para pacotes leves e compactos
            self.transporte = transporte_aereo()