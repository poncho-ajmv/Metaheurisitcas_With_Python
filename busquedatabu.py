import networkx as nx
import matplotlib.pyplot as plt
import random

def calculate_mst_cost(G, edges):
    """Calculates the total cost of a spanning tree defined by the given edges."""
    return sum(G[u][v]['weight'] for u, v in edges)

def get_mst_edges(G):
    """Computes the Minimum Spanning Tree (MST) edges using Kruskal's algorithm."""
    return list(nx.minimum_spanning_edges(G, algorithm='kruskal', data=False))

def generate_neighbors(G, current_edges):
    """Generates neighbors by swapping edges."""
    all_edges = list(G.edges)
    neighbors = []
    
    for edge_to_remove in current_edges:
        for edge_to_add in all_edges:
            if edge_to_add not in current_edges:
                new_edges = current_edges.copy()
                new_edges.remove(edge_to_remove)
                new_edges.append(edge_to_add)
                if nx.is_connected(nx.Graph(new_edges)):
                    neighbors.append(new_edges)
    return neighbors

def tabu_search_mst(G, iterations=20, tabu_size=5):
    current_edges = get_mst_edges(G)
    best_edges = current_edges[:]
    best_cost = calculate_mst_cost(G, best_edges)
    tabu_list = []
    
    pos = {'A': (-1, 1), 'B': (0, 2), 'C': (0, 0), 'D': (0, -2), 'E': (1, 1)}
    plt.ion()
    fig, ax = plt.subplots()
    
    visualize_graph(G, best_edges, pos, ax, 0, calculate_mst_cost(G, best_edges), best_cost, first=True)
    
    for i in range(iterations):
        neighbors = generate_neighbors(G, current_edges)
        best_neighbor = None
        best_neighbor_cost = float('inf')
        
        for neighbor in neighbors:
            if neighbor not in tabu_list:
                cost = calculate_mst_cost(G, neighbor)
                if cost < best_neighbor_cost:
                    best_neighbor = neighbor
                    best_neighbor_cost = cost
        
        if best_neighbor:
            current_edges = best_neighbor[:]
            if best_neighbor_cost < best_cost:
                best_edges = best_neighbor[:]
                best_cost = best_neighbor_cost
            
            tabu_list.append(best_neighbor)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)
        
        visualize_graph(G, current_edges, pos, ax, i + 1, calculate_mst_cost(G, current_edges), best_cost)
    
    visualize_final_solution(G, best_edges, pos, ax, best_cost)
    plt.ioff()
    plt.show()
    return best_edges, best_cost

def visualize_graph(G, edges, pos, ax, iteration, cost, best_cost, first=False):
    ax.clear()
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='white', edge_color='black', ax=ax, node_size=1500, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax, font_size=10)
    edge_color = 'g' if first else 'r'
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_color, width=2, ax=ax, style='dashed')
    ax.set_title(f"Iteration {iteration}\nCurrent Cost: {cost}\nBest Cost So Far: {best_cost}")
    plt.pause(1)

def visualize_final_solution(G, edges, pos, ax, cost):
    ax.clear()
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='white', edge_color='black', ax=ax, node_size=1500, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax, font_size=10)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='g', width=3, ax=ax, style='dashed')
    ax.set_title(f"Best Solution Found\nBest Cost: {cost}")
    plt.pause(2)

# Create graph
G = nx.Graph()
G.add_weighted_edges_from([
    ('A', 'B', 20), ('A', 'C', 10), ('A', 'D', 15),
    ('B', 'E', 30), ('C', 'D', 25), ('C', 'E', 5),
    ('D', 'E', 40)
])

best_edges, best_cost = tabu_search_mst(G, iterations=20, tabu_size=5)
print("Best edges:", best_edges)
print("Best cost:", best_cost)