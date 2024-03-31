from src.models import Plantacao
from src.sensores.sensoriamento import gerar
from src.operacoes import (
    imprimir_plantacao,
    imprimir_temperatura,
    imprimir_status,
    sort_temperaturas,
    PlantacaoTemperatura,
)

TOTAL_PLANTACAO = 10
TOTAL_LEITURA = 10


"""
    Gerando a leitura de N plantações
    contendo X leituras de temperatura

    Complexidade: O(N²)

    Esta função tem uma complexidade quadrática O(N²)
    Pois tem 2 loops aninhados:
    1º loop para criar as plantações
    2º loop para criar as leituras de temperatura
    E retorna uma lista de tuplas contendo plantação e temperaturas
"""


def leitura_das_plantacoes() -> list[PlantacaoTemperatura]:
    plantacoes = []
    for i in range(TOTAL_PLANTACAO):
        plantacao = Plantacao(
            nome=f"Plantacao_{i+1}",
        )

        temperatura = gerar(TOTAL_LEITURA)

        plantacoes.append(PlantacaoTemperatura(plantacao, temperatura))

    return plantacoes


def fase_1_plantacoes(plantacoes: list[PlantacaoTemperatura]):
    print("\n", "-" * 50, "\n")
    imprimir_plantacao(plantacoes)


"""
    Usa a função imprimir_temperatura com a complexidade O(N²)
"""


def fase_2_temperaturas_desordenadas(plantacoes: list[PlantacaoTemperatura]):
    imprimir_temperatura(plantacoes)


"""
    Usa a função sort_temperaturas com a complexidade O(N²)
"""


def fase_2_1_temperaturas_ordenadas(plantacoes: list[PlantacaoTemperatura]):
    print("\n", "-" * 50, "\n")
    plantacoes_ordenadas = sort_temperaturas(plantacoes)
    imprimir_temperatura(plantacoes_ordenadas)


"""
    Usa a função imprimir_status com a complexidade O(N³)
"""


def fase_3_status(plantacoes: list[PlantacaoTemperatura]):
    print("\n", "-" * 50, "\n")
    imprimir_status(plantacoes)


def main():
    plantacoes = leitura_das_plantacoes()

    fase_1_plantacoes(plantacoes)
    fase_2_temperaturas_desordenadas(plantacoes)
    fase_2_1_temperaturas_ordenadas(plantacoes)
    fase_3_status(plantacoes)


if __name__ == "__main__":
    main()
