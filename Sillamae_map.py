
# "Gagarini_33"
# "Kutsehariduskeskus"
# "Olerex"
# "Skola_nr_4"
# "Dom_kultury"
# "Promenad"
# "Zavod"
# "Sputnik"
# "Druzhba"
# "Vodopad"


# "Gagarini_33"
# "Olerex"
# "Druzhba"

checkpoints_graph_weighted = {
    "Gagarini_33": {"Druzhba": 3.6, "Olerex": 1.5, "Kutsehariduskeskus": 0.65},
    "Druzhba": {"Gagarini_33": 3.6, "Olerex": 2.1, "Kutsehariduskeskus": 3.3},
    "Olerex": {"Druzhba": 2.1, "Gagarini_33": 1.5, "Kutsehariduskeskus": 1.2},
    "Kutsehariduskeskus": {"Gagarini_33": 0.65, "Druzhba": 3.3, "Olerex": 1.2}
}

# setting distances to infinity
inf = 100
distances = {
    "Gagarini_33": 0,
    "Olerex": inf,
    "Druzhba": inf,
    "Kutsehariduskeskus": inf
}

# setting nodes to unvisited

unvisited = {
    "Gagarini_33": True,
    "Olerex": True,
    "Druzhba": True,
    "Kutsehariduskeskus": True
}

while any(unvisited.values()) is True:
    unvisited_nodes = (node for node in unvisited if unvisited[node])   #generator object
    unvisited_nodes_list = list(unvisited_nodes)
    current_node = min(unvisited_nodes_list, key=lambda x: distances[x])

    print("Unvisited nodes: ", unvisited_nodes_list)
    print("Current node: ", current_node)

    neighbors_and_weights = checkpoints_graph_weighted[current_node].items()
    print("Neighbors and weights: ", neighbors_and_weights)

    for neighbor, weight in neighbors_and_weights:
        if distances[current_node] + weight < distances[neighbor]:
            new_distance = distances[current_node] + weight
            distances[neighbor] = new_distance

    unvisited[current_node] = False

print(f"Distances from starting point: {distances}")