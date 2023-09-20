import networkx as nx


def is_cycle(graph, sequence):
    if len(sequence) <= 2:
        return False
    return sequence[0] in graph[sequence[-1]]


def is_simple_cycle(graph, sequence):
    if len(sequence) < 3:
        return False
    if sequence[0] == sequence[-1] and len(set(sequence)) == len(sequence):
        return True
    return False


def d(graph, sequence):
    
    result = []
    
    if nx.is_path(graph, sequence):
        result.append("Маршрут")
    
    # Проверяем, является ли последовательность цепью
    if nx.is_simple_path(graph, sequence):
        result.append("Цепь")

    # Проверяем, является ли последовательность простой цепью
    if nx.is_simple_path(graph, sequence) and len(set(sequence)) == len(sequence):
        result.append("Простая цепь")

    # Проверяем, является ли последовательность циклом
    if is_cycle(graph, sequence):
        result.append("Цепь")

    if is_simple_cycle(graph, sequence):
        result.append("Простой цикл")
        
    # Если ни одно из условий не выполнилось, вернем "Неизвестно"
    return result


G = nx.Graph()

graph = [(1,2), (1,7), (1,6), (1, 4), (2,3), (2,4), (3, 5), (3, 6), (3, 4), (5, 4), (6, 7)]

sequence = [6,7,1,4,3,2]

sequences = [
    [6,7,1,4,3,2],
    [2,1,7,6,1,4],
    [1,2,3,4,1],
    [1,2,3,4,2,1],
    [2,1,6,7,1,4,2]
]


G.add_edges_from(graph)

n = 0
for sequence in sequences:
    seq_t = d(G, sequence)
    n += 1
    for i in range(len(seq_t)):
        print(f"Последовательность {n} - {seq_t[i]}")
    print()
