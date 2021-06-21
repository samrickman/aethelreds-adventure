
# Purpose of script is just to plot a quick network graph
# of what has been implemented. When completed it should show
# the entire game.
import matplotlib.pyplot as plt
import networkx as nx
import os
import json

room_dir = "../rooms/"
files = os.listdir(room_dir)

# Get nodes and edges from json files
edges = []
labels = {}
for file in files:
    with open(f"{room_dir}{file}", "r") as f:
        room = json.load(f)
        #if room['type'] != 'choices':
        #    next
    choices = room['choices']
    room_edges = [(room['name'], choice) for choice in choices.values()]
    
    room_labels = {(room['name'], choice[1]) : choice[0] for choice in choices.items()}
    edges = edges + room_edges
    try:
        labels = labels | room_labels # python 3.9+ only
    except TypeError:
        labels = {**labels, **room_labels}

G = nx.DiGraph()
G.add_edges_from(edges)
pos = nx.spring_layout(G, k=1, iterations = 50)
plt.figure(figsize=(20,20))    
nx.draw(G,
    pos,
    edge_color='black',
    width=1,
    linewidths=1,
    node_size=1000,
    node_color='lightblue',
    alpha=0.9,
    font_size = 30,
    labels={node:node for node in G.nodes()})
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels,
    font_color='red',
    font_size = 18)
plt.axis('off')

plt.savefig("schema.png", format="PNG")