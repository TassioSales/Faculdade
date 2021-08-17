"""Implementação em Python 3 do algoritmo de Djikstra para encontrar o mais curto caminho entre os nós em um gráfico. Escrito como um exercício de aprendizagem, muitos comentários e sem tratamento de erros.
"""
# 24/05/2021
# ALUNOS: TASSIO SALES, PEDRO MAGALHAES, ROBSON LUIS


from collections import deque

INFINITY = float("inf")


class Graph:
    def __init__(self, filename):
        """Lê a definição do gráfico e a armazena. Cada linha do gráfico
        arquivo de definição define uma borda especificando o nó inicial,
        nó final e distância, delimitado por espaços.

        Armazena a definição do gráfico em duas propriedades que são usadas por
        O algoritmo de Dijkstra no método shortest_path:
        self.nodes = conjunto de todos os nós únicos no gráfico
        self.adjacency_list = dict que mapeia cada nó para um conjunto não ordenado de
        (vizinho, distância) tuplas. """

        # Leia o arquivo de definição de gráfico e armazene em graph_edges como uma lista de
        # listas de [from_node, to_node, distance]. Esta estrutura de dados não é
        # usado pelo algoritmo de Dijkstra, é apenas uma etapa intermediária no
        # criar self.nodes e self.adjacency_list.
        graph_edges = []
        with open(filename) as fhandle:
            for line in fhandle:
                edge_from, edge_to, cost, *_ = line.strip().split(" ")
                graph_edges.append((edge_from, edge_to, float(cost)))

        self.nodes = set()
        for edge in graph_edges:
            self.nodes.update([edge[0], edge[1]])

        self.adjacency_list = {node: set() for node in self.nodes}
        for edge in graph_edges:
            self.adjacency_list[edge[0]].add((edge[1], edge[2]))

    def shortest_path(self, start_node, end_node):
        """Usa o algoritmo de Dijkstra para determinar o caminho mais curto de
        start_node para end_node. Retorna (caminho, distância)
        """

        # Todos os nós são inicialmente não visitados.
        unvisited_nodes = self.nodes.copy()

        # Crie um dicionário da distância de cada nó de start_node. Nós vamos
        # atualize a distância de cada nó sempre que encontrarmos um caminho mais curto.
        distance_from_start = {
            node: (0 if node == start_node else INFINITY) for node in self.nodes
        }

        # Initialize previous_node, o dicionário que mapeia cada nó para o
        # nó foi visitado a partir do momento em que o caminho mais curto para ele foi encontrado.
        previous_node = {node: None for node in self.nodes}

        while unvisited_nodes:

            # Defina current_node para o nó não visitado com a distância mais curta
            # calculado até agora.
            current_node = min(
                unvisited_nodes, key=lambda node: distance_from_start[node]
            )
            unvisited_nodes.remove(current_node)

            # Se a distância de current_node for INFINITY, o restante não visitado
            # nós não estão conectados a start_node, então terminamos.
            if distance_from_start[current_node] == INFINITY:
                break

            # Para cada vizinho de current_node, verifique se a distância total
            # para o vizinho via current_node é menor que a distância que nós
            # atualmente tem para esse nó. Se for, atualize os valores do vizinho
            # para distance_from_start e previous_node.
            for neighbor, distance in self.adjacency_list[current_node]:
                new_path = distance_from_start[current_node] + distance
                if new_path < distance_from_start[neighbor]:
                    distance_from_start[neighbor] = new_path
                    previous_node[neighbor] = current_node

            if current_node == end_node:
                break  # visitamos o nó de destino, então terminamos

        # Para construir o caminho a ser retornado, iteramos através dos nós de
        # end_node de volta para start_node. Observe o uso de um deque, que pode
        # appendleft com desempenho O (1).
        path = deque()
        current_node = end_node
        while previous_node[current_node] is not None:
            path.appendleft(current_node)
            current_node = previous_node[current_node]
        path.appendleft(start_node)

        return path, distance_from_start[end_node]


def main():
    """Executa alguns testes simples para verificar a implementação..
    """
    verify_algorithm(
        filename="gráfico_ simples.txt",
        start="A",
        end="G",
        path=["A", "D", "E", "G"],
        distance=11,
    )
    verify_algorithm(
        filename="seattle_area.txt",
        start="Renton",
        end="Redmond",
        path=["Renton", "Factoria", "Bellevue", "Northup", "Redmond"],
        distance=16,
    )
    verify_algorithm(
        filename="seattle_area.txt",
        start="Seattle",
        end="Redmond",
        path=["Seattle", "Eastlake", "Northup", "Redmond"],
        distance=15,
    )
    verify_algorithm(
        filename="seattle_area.txt",
        start="Eastlake",
        end="Issaquah",
        path=["Eastlake", "Seattle", "SoDo", "Factoria", "Issaquah"],
        distance=21,
    )


def verify_algorithm(filename, start, end, path, distance):
    """Função auxiliar para executar testes simples e imprimir resultados no console.

    filename = arquivo de definição de gráfico
    start/end = caminho a ser calculado
    path = caminho curto esperado
    distance = distância esperada do caminho
    """
    graph = Graph(filename)
    returned_path, returned_distance = graph.shortest_path(start, end)

    assert list(returned_path) == path
    assert returned_distance == distance

    print('\narquivo de definição de gráfico: {0}'.format(filename))
    print('      nós inicial / final: {0} -> {1}'.format(start, end))
    print('        caminho mais curto: {0}'.format(path))
    print('       distância total: {0}'.format(distance))


if __name__ == "__main__":
    main()
