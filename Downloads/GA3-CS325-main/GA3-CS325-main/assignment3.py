'''
    For testing he'll put it in a different directory, call <three_min_spanning_trees>,
    then check its output or whatever lmao
'''

def three_min_spanning_trees(input_file_path, output_file_path):
    def find(parent, node):
        if parent[node] != node:
            parent[node] = find(parent, parent[node])  # Path compression
        return parent[node]

    def union(parent, rank, node1, node2):
        root1 = find(parent, node1)
        root2 = find(parent, node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True
        return False

    def kruskal_algorithm(vertex_count, edges, excluded_edges=set()):
        parent = list(range(vertex_count))
        rank = [0] * vertex_count
        total_weight = 0
        selected_edges = []

        for node1, node2, weight in edges:
            if (node1, node2) not in excluded_edges and (node2, node1) not in excluded_edges:
                if union(parent, rank, node1, node2):
                    total_weight += weight
                    selected_edges.append((node1, node2, weight))
        return total_weight, selected_edges

    adjacency_matrix = []
    with open(input_file_path, 'r') as file:
        vertex_count = int(file.readline().strip())
        for line in file:
            adjacency_matrix.append([int(x) for x in line.strip().split(',')])

    edge_list = []
    for i in range(vertex_count):
        for j in range(i):
            if adjacency_matrix[i][j] > 0:
                edge_list.append((i, j, adjacency_matrix[i][j]))

    edge_list.sort(key=lambda x: x[2])

    mst_weight1, mst_edges1 = kruskal_algorithm(vertex_count, edge_list)

    mst_weight2 = float('inf')
    for node1, node2, _ in mst_edges1:
        excluded_edges = {(node1, node2)}
        mst_weight_temp, _ = kruskal_algorithm(vertex_count, edge_list, excluded_edges)
        if mst_weight_temp < mst_weight2:
            mst_weight2 = mst_weight_temp

    mst_weight3 = float('inf')
    for i in range(len(mst_edges1)):
        for j in range(i + 1, len(mst_edges1)):
            excluded_edges = {(mst_edges1[i][0], mst_edges1[i][1]), (mst_edges1[j][0], mst_edges1[j][1])}
            mst_weight_temp, _ = kruskal_algorithm(vertex_count, edge_list, excluded_edges)
            if mst_weight_temp < mst_weight3 and mst_weight_temp != float('inf'):
                mst_weight3 = mst_weight_temp

    if mst_weight3 == float('inf'):
        mst_weight3 = float('inf')

    with open(output_file_path, 'w') as file:
        file.write(f"{mst_weight1}\n")
        file.write(f"{mst_weight2}\n")
        file.write(f"{mst_weight3}\n")

    print(mst_weight1)
    print(mst_weight2)
    print(mst_weight3)

# Example usage
three_min_spanning_trees("test_cases/input2.txt", "test_cases/output.txt")