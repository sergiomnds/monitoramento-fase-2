"""
Funções de operações
"""

from collections import namedtuple

PlantacaoTemperatura = namedtuple("PlantacaoTemperatura", ["plantacao", "temperaturas"])


"""
    Imprime as plantações
    :param data: lista de tuplas contendo plantação e temperaturas
    :return: None

    Complexidade: O(N)

    Esta função tem uma complexidade linear O(N)
    Pois tem apenas 1 loop para imprimir as plantações
"""


def imprimir_plantacao(data: PlantacaoTemperatura):
    for d in data:
        print(f"Plantacao: {d.plantacao}")


"""
    Imprime as plantações e suas respectivas temperaturas
    :param data: lista de tuplas contendo plantação e temperaturas
    :return: None

    Complexidade: O(N²)

    Esta função tem uma complexidade quadrática O(N²)
    Pois tem 2 loops aninhados:
    1º loop para pegar as plantações e temperaturas (na qual é uma lista)
    2º loop para capturar as temperaturas da lista
    E imprime o nome da plantação e a temperatura
"""


def imprimir_temperatura(data: list[PlantacaoTemperatura]):
    for d in data:
        print(f"Plantacao: {d.plantacao}")
        for temperatura in d.temperaturas:
            status_temperatura = verifica_temperatura(temperatura.get_value())
            print(f"Temperatura: {temperatura} - {status_temperatura}")
        print("\n")


"""
    Verifica a temperatura e retorna o status
    :param temperatura: float
    :return: str

    Complexidade: O(1)

    A complexidade desta fução é constante O(1),
    pois realiza um núero fixo de operações independentemente do valor de entrada.
"""


def verifica_temperatura(temperatura: float) -> str:
    if temperatura < 20.0:
        return "Frio"
    elif temperatura >= 20.0 and temperatura <= 30.0:
        return "Ideal"
    else:
        return "Muito Quente"

"""
    Algoritmo de ordenação Quick Sort
    :param data: lista de objetos Temperatura
    :return: lista de objetos Temperatura ordenados

    Complexidade: O(nLog(n))

    A complexidade de tempo da função quick_sort_temperaturas é O(nlog(n)),
    onde n é o número de objetos Temperatura na lista data.

    Isso ocorre porque a função usa o algoritmo Quick Sort,
    que tem uma complexidade de tempo de O(n*log(n)) no caso médio.
    A função particiona a lista data em duas sub-listas, cada uma contendo os
    elementos que são menores ou maiores que o pivô,
    e então ordena recursivamente essas sub-listas.
"""


def quick_sort_temperaturas(temperaturas: list):
    if len(temperaturas) <= 1:
        return temperaturas
    else:
        pivot = temperaturas[0]
        less_than_pivot = [
            element for element in temperaturas[1:] if element.value < pivot.value
        ]
        greater_than_pivot = [
            element for element in temperaturas[1:] if element.value > pivot.value
        ]
        return (
            quick_sort_temperaturas(less_than_pivot)
            + [pivot]
            + quick_sort_temperaturas(greater_than_pivot)
        )


"""
    Ordena as temperaturas de cada plantação
    :param data: lista de tuplas contendo plantação e temperaturas
    :return: lista de tuplas contendo plantação e temperaturas ordenadas

    Complexidade: O(nmLog(m))

    onde n é o número de PlantacaoTemperatura na lista data,
    e m é o número médio de objetos Temperatura na lista temperaturas de cada PlantacaoTemperatura.

    Isso ocorre porque a função contém um loop que é executado n vezes, e dentro deste loop,
    ela chama a função quick_sort_temperaturas, que tem uma complexidade de tempo de O(mlog(m)),
    onde m é o número de objetos Temperatura na lista temperaturas.

    Portanto, a complexidade de tempo geral é O(nm*log(m)).

"""


def sort_temperaturas(data: list[PlantacaoTemperatura]):
    for plantacao, temperaturas in data:
        temperaturas = quick_sort_temperaturas(temperaturas)
        yield PlantacaoTemperatura(plantacao, temperaturas)
