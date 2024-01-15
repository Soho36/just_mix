# FIND THE SHORTEST WAY
underground_map_weighted = {
    "admiralteiskaja": {"sadovaja": 4},
    "sadovaja": {"sennaja": 4, "spasskaja": 3, "admiralteiskaja": 4, "zvenigorodskaja":5},
    "sennaja": {"sadovaja": 4, "spasskaja": 4},
    "spasskaja": {"sadovaja": 3, "sennaja": 4, "dostoevskaja": 6},
    "dostoevskaja": {"spasskaja": 6, "vladimirskaja": 3},
    "vladimirskaja": {"dostoevskaja": 3, "pushkinskaja": 4},
    "pushkinskaja": {"zvenigorodskaja": 3, "vladimirskaja": 4},
    "zvenigorodskaja": {"pushkinskaja": 3, "sadovaja": 5}
}
inf = 1000
# set distances to infinity
distances = {"admiralteiskaja": 0,
             "sadovaja": inf,
             "sennaja": inf,
             "spasskaja": inf,
             "zvenigorodskaja": inf,
             "dostoevskaja": inf,
             "vladimirskaja": inf,
             "pushkinskaja": inf,
             }

# set all nodes as unvisited
unvisited = {"admiralteiskaja": True,
             "sadovaja": True,
             "sennaja": True,
             "spasskaja": True,
             "zvenigorodskaja": True,
             "dostoevskaja": True,
             "vladimirskaja": True,
             "pushkinskaja": True,
             }

while any(unvisited.values()):
    # Find the unvisited node with the smallest distance
    current_node = min(
        (node for node in unvisited if unvisited[node]), key=lambda x: distances[x]
    )

    # Update distances to neighbors if a shorter path is found
    for neighbor, weight in underground_map_weighted[current_node].items():
        if distances[current_node] + weight < distances[neighbor]:
            distances[neighbor] = distances[current_node] + weight

    # Mark the current node as visited
    unvisited[current_node] = False

print(distances)