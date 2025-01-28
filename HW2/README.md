# Longest Path in a Directed Acyclic Graph (DAG)

This project contains a Python program that calculates:

1. The length of the longest path in a weighted directed acyclic graph (DAG) from node `1` to node `n`.
2. The number of distinct paths from node `1` to node `n` that have the longest length.

## Features

- Efficient computation using adjacency lists and topological sorting.
- Linear time complexity relative to the number of nodes and edges.
- Supports large graph inputs.

## Requirements

- Python 3.6 or later.

## Files

- `main.py`: The Python script containing the program.
- `inSample1.txt`, `inSample2.txt`: Example input files.

## Usage

### Running the Program

1. Ensure you have Python installed.
2. Place your input file in the same directory as the script.
3. Run the script:

```bash
python main.py
```

4. Enter the name of the input file when prompted, e.g., `inSample1.txt`.

### Input Format

The input file must have the following format:

- The first line contains two integers `N` (number of nodes) and `M` (number of edges).
- The next `M` lines each contain three integers `u`, `v`, `w`:
  - `u`: Start node of the edge.
  - `v`: End node of the edge.
  - `w`: Weight of the edge.

### Output

The program prints two numbers:

1. The length of the longest path.
2. The number of distinct paths of that length.

### Example

#### Input (inSample1.txt):
```
5 6
1 2 3
1 3 6
2 4 4
3 4 2
4 5 5
3 5 8
```

#### Command:
```bash
python main.py
```

#### Output:
```
16 1
```

## Notes

- The input graph must be a directed acyclic graph (DAG).
- The graph is represented using an adjacency list internally for optimal performance.

## License

This project is provided for educational purposes and does not come with a license for commercial use.

