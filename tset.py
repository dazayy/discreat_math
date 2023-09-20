import networkx as nx
import matplotlib.pyplot as plt

# Создаем ненаправленный граф
G = nx.Graph()

# Добавляем вершины

graph = [(1,2), (1,7), (1,6), (1, 4), (2,3), (2,4), (3, 5), (3, 6), (3, 4), (5, 4), (6, 7)]

sequence = [6,7,1,4,3,2]


# # Добавляем рёбра
# G.add_edge(1, 2)  # Добавляем ребро между вершинами 1 и 2
# G.add_edge(2, 3)  # Добавляем ребро между вершинами 2 и 3

# Можно также добавить рёбра сразу для нескольких вершин
G.add_edges_from(graph)

# Теперь в графе G есть вершины 1, 2, 3 и следующие рёбра: (1, 2), (1, 3), (2, 3)

# Рисуем граф
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=12, font_color="black", font_weight="bold")
nx.draw_networkx_edges(G, pos, edgelist=[(1, 2), (2, 3)], width=2, edge_color="red")
nx.draw_networkx_edges(G, pos, edgelist=[(1, 3), (1, 2), (2, 3)], width=1, edge_color="gray")

# Отображаем граф
plt.axis('off')
plt.show()
