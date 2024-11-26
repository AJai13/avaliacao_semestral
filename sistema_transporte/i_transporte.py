from abc import ABC, abstractmethod


class iTransporte(ABC):
    @abstractmethod
    def entregar(self, encomenda):
        pass
