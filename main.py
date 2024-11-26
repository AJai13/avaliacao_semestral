from sistema_transporte import transporte_terrestre
from sistema_transporte.sistema import sistema_de_transporte
from sistema_transporte.transporte_terrestre import transporte_terrestre
from sistema_transporte.transporte_aereo import transporte_aereo
from sistema_transporte.transporte_maritimo import transporte_maritimo
from sistema_transporte.transporte_drones import transporte_drones


if __name__ == "__main__":
    sistema = sistema_de_transporte()

    encomenda1 = {
        "descricao": "Livro",
        "peso": 2,
        "dimensoes": (30, 20, 5),
        "local": "área metropolitana",
        "destino": "nacional",
    }
    encomenda2 = {
        "descricao": "Televisão",
        "peso": 25,
        "dimensoes": (80, 60, 40),
        "local": "zona rural",
        "destino": "nacional",
    }

    encomenda3 = {
        "descricao": "Máquina de lavar",
        "peso": 50,
        "dimensoes": (100, 70, 60),
        "local": "porto",
        "destino": "internacional",
    }

    print(
        f"\nSeleção Dinâmica para encomendas: {encomenda1['descricao']}, {encomenda2['descricao']}, {encomenda3['descricao']}"
    )
    # Seleção dinâmica de transporte para encomenda1
    sistema.selecionar_transporte(encomenda1)
    print(sistema.entregar(encomenda1))

    # Seleção dinâmica de transporte para encomenda2
    sistema.selecionar_transporte(encomenda2)
    print(sistema.entregar(encomenda2))

    # Seleção dinâmica de transporte para encomenda3
    sistema.selecionar_transporte(encomenda3)
    print(sistema.entregar(encomenda3))

    print(
        "--------------------------------------------------------------------------\n"
    )


    print('Seleção Manual: ')
    print('\n')
    print('Transporte terrestre:')
    # Transporte terrestre
    sistema.set_transporte(
        transporte_terrestre(transportadora_local="Transportadora Narcos")
    )
    print(sistema.entregar(encomenda1))
    print(sistema.entregar(encomenda2))
    print(sistema.entregar(encomenda3))

    print(
        "--------------------------------------------------------------------------\n"
    )

    print('Transporte aéreo:')
    # Transporte aéreo
    sistema.set_transporte(transporte_aereo())
    print(sistema.entregar(encomenda1))
    print(sistema.entregar(encomenda2))
    print(sistema.entregar(encomenda3))
    print(
        "--------------------------------------------------------------------------\n"
    )

    print('Transporte marítmo:')
    # Transporte marítimo
    sistema.set_transporte(transporte_maritimo())
    print(sistema.entregar(encomenda1))
    print(sistema.entregar(encomenda2))
    print(sistema.entregar(encomenda3))
    print(
        "--------------------------------------------------------------------------\n"
    )

    print('Transporte por drones:')
    # Transporte por drones
    sistema.set_transporte(transporte_drones())
    print(sistema.entregar(encomenda1))
    print(sistema.entregar(encomenda2))
    print(sistema.entregar(encomenda3))
    print(
        "--------------------------------------------------------------------------\n"
    )
