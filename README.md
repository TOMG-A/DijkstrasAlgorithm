# Dijkstra's Algorithm Implementation

A simple Dijkstra's Algorithm implementation

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the package.

```bash
pip install -i https://test.pypi.org/simple/ dijkstras-algorithm-TOMG-A
```

## Usage

```python
from dijkstra import *

NodeA=Node("A")
graph=Graph(NodeA)
dist,prev,_=Dijkstra(graph,NodeA)
```

## License

[MIT]([https://choosealicense.com/licenses/mit/](https://github.com/TOMG-A/DijkstrasAlgorithm/blob/main/LICENSE))

[![Upload Python Package](https://github.com/TOMG-A/DijkstrasAlgorithm/actions/workflows/python-publish.yml/badge.svg)](https://github.com/TOMG-A/DijkstrasAlgorithm/actions/workflows/python-publish.yml)
