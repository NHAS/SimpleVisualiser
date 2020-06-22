import networkx as nx
import matplotlib.pyplot as plt
import json
import sys
import random

G = nx.Graph()

node_color_map = []
dup = 0
with open('data.json') as json_file:
    data = json.load(json_file)
    for k, v in data.items():
        if (len(sys.argv) == 2 and k != sys.argv[1]):
            continue

        G.add_node(k)
        node_color_map.append("#34c0eb")

        hex_color = "#%06x" % random.randint(0, 0xFFFFFF)
        for nick in v:
            if G.has_node(nick):
                dup += 1

            if not G.has_node(nick):
                node_color_map.append("#52b519")

            G.add_edge(k, nick, color=hex_color)

print("Nodes of graph: ")
print(len(G.nodes()))
print(len(node_color_map))
print(dup)

edges = G.edges()
colors = [G[u][v]['color'] for u, v in edges]

nx.draw(G, edge_color=colors,
        node_color=node_color_map, with_labels=True)
plt.show()  # display
