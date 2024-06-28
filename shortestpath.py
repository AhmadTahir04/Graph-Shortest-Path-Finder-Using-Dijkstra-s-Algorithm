def dijkstra(vertices, edges, start, end):
    # Initialize distances and previous vertices for each vertex in the graph
    # Set initial distances to infinity and previous vertices to None
    distances = {vertex: float('infinity') for vertex in vertices}
    previous = {vertex: None for vertex in vertices}

    # Initialize a dictionary to store the neighbors and corresponding edge weights for each vertex
    vi_neighbors_distance = {vertex: [] for vertex in vertices}
    distances[start] = 0  # Set the distance from the start vertex to itself as 0

    # Populate the neighbors and their distances for each vertex
    for u, v, weight in edges:
        vi_neighbors_distance[u].append((v, weight))
        vi_neighbors_distance[v].append((u, weight))

    # Create a list of all unvisited vertices
    unvisited = vertices[:]

    # Iterate as long as there are unvisited vertices
    while unvisited:
        # Find the unvisited vertex with the smallest known distance from the start vertex
        current_vertex = None
        current_min_distance = float('infinity')
        for vertex in unvisited:
            if distances[vertex] < current_min_distance:
                current_min_distance = distances[vertex]
                current_vertex = vertex

        # Break the loop if the smallest distance is infinity (unreachable vertex) or the end vertex is reached
        if current_min_distance == float('infinity') or current_vertex == end:
            break

        # Remove the current vertex from the list of unvisited vertices
        unvisited.remove(current_vertex)

        # Update the distances of the neighboring vertices of the current vertex
        for neighbor, weight in vi_neighbors_distance[current_vertex]:
            alternative_route = distances[current_vertex] + weight
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                previous[neighbor] = current_vertex

    # Reconstruct the shortest path from the end vertex to the start vertex
    path, current_vertex = [], end
    while current_vertex and previous[current_vertex] is not None:
        path.insert(0, current_vertex)
        current_vertex = previous[current_vertex]
    if path:
        path.insert(0, current_vertex)

    # Return the shortest distance and the shortest path
    return distances[end], path

# Example usage
vertices = ["v0", "v1", "v2", "v3", "v4", "v5"] # List of vertices
edges = [("v1", "v2", 2), ("v2", "v3", 3), ("v3", "v4", 1), ("v4", "v5", 5), ("v1", "v3", 6), ("v0", "v1", 7)]  # Example edges
start_vertex, end_vertex = "v1", "v0"  # Start at v1 and end at v0

# Compute shortest path
distance, path = dijkstra(vertices, edges, start_vertex, end_vertex)
print("Shortest Distance:", distance)
print("Shortest Path:", path)
