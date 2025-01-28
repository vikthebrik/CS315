from collections import defaultdict, deque
import sys

def find_longest_path_and_count(n, edges):
    # Initialize adjacency list and in-degrees
    adj_list = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    # Build graph
    for u, v, w in edges:
        adj_list[u].append((v, w))
        in_degree[v] += 1

    # Topological sort using Kahn's algorithm
    topo_sort = []
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])

    while queue:
        node = queue.popleft()
        topo_sort.append(node)
        for neighbor, _ in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Initialize DP arrays
    longest_path = [-sys.maxsize] * (n + 1)
    path_count = [0] * (n + 1)
    longest_path[1] = 0  # Start at node 1
    path_count[1] = 1

    # Process nodes in topological order
    for node in topo_sort:
        for neighbor, weight in adj_list[node]:
            if longest_path[node] + weight > longest_path[neighbor]:
                longest_path[neighbor] = longest_path[node] + weight
                path_count[neighbor] = path_count[node]
            elif longest_path[node] + weight == longest_path[neighbor]:
                path_count[neighbor] += path_count[node]

    # Return results for node n
    return longest_path[n], path_count[n]

# Receive Input, Print outputs
def main():
    file_name = input("Enter the input file name: ")
    try:
        with open(file_name, "r") as f:
            data = f.readlines()

        n, m = map(int, data[0].split())
        edges = [tuple(map(int, line.split())) for line in data[1:]]

        longest_length, count = find_longest_path_and_count(n, edges)
        print("Longest Length:", longest_length)
        print("Count:", count)
    except FileNotFoundError:
        print("File not found. Please try again.")

if __name__ == "__main__":
    main()
