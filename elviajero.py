import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import string
import tkinter as tk
from tkinter import simpledialog

def factorial(n):
    return math.factorial(n - 1) // 2

def generate_random_edges(cities):
    edges = []
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            edges.append((cities[i], cities[j], random.randint(5, 15)))
    return edges

def calculate_distance(route, graph):
    distance = 0
    for i in range(len(route) - 1):
        if graph.has_edge(route[i], route[i+1]):
            distance += graph[route[i]][route[i+1]]['weight']
    return distance

def reverse_subtour(route, graph):
    best_route = route[:]
    best_distance = calculate_distance(route, graph)
    improved = True
    iterations = []
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]
                new_distance = calculate_distance(new_route, graph)
                if new_distance < best_distance:
                    best_route = new_route[:]
                    best_distance = new_distance
                    improved = True
                    iterations.append((new_route, new_distance))
        route = best_route[:]
    return best_route, best_distance, iterations

def draw_tsp_graph():
    root = tk.Tk()
    root.withdraw()
    
    while True:
        try:
            num_cities = simpledialog.askinteger("Entrada", "Ingrese el número de nodos (mínimo 3):", minvalue=3)
            if num_cities:
                break
        except ValueError:
            continue
    
    G = nx.Graph()
    cities = list(string.ascii_uppercase[:num_cities])
    G.add_nodes_from(cities)
    edges = generate_random_edges(cities)
    
    for edge in edges:
        G.add_edge(edge[0], edge[1], weight=edge[2])
    
    pos = nx.spring_layout(G, seed=42)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(left=0, bottom=0, right=0.5, top=1)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, edge_color='gray', ax=ax)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)
    
    total_routes = factorial(num_cities)
    ax.set_title(f"Problema del Agente Viajero\nNodos: {num_cities}, Rutas posibles: {total_routes}")
    
    # Generar una solución inicial aleatoria
    initial_route = cities + [cities[0]]
    initial_distance = calculate_distance(initial_route, G)
    
    # Dibujar la solución inicial
    path_edges = [(initial_route[i], initial_route[i+1]) for i in range(len(initial_route)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2, ax=ax)
    
    # Aplicar algoritmo de subviaje inverso
    best_route, best_distance, iterations = reverse_subtour(initial_route, G)
    
    # Mostrar cálculos en la figura
    text = f"Ruta Inicial: {initial_route}\nDistancia: {initial_distance}\n\nIteraciones:\n"
    for i, (route, dist) in enumerate(iterations):
        text += f"Iteración {i+1}: {route} - Distancia: {dist}\n"
    text += f"\nMejor Ruta: {best_route} - Distancia: {best_distance}"
    
    ax.text(1.05, 0.5, text, transform=ax.transAxes, fontsize=10, verticalalignment='center', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.show()

# Ejecutar la visualización
draw_tsp_graph()
