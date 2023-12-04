# Dijkstra's Algorithm Implementation
[![Upload Python Package](https://github.com/TOMG-A/DijkstrasAlgorithm/actions/workflows/python-publish.yml/badge.svg)](https://github.com/TOMG-A/DijkstrasAlgorithm/actions/workflows/python-publish.yml)
[![Sample Project - View](https://img.shields.io/badge/Sample_Project-View-informational?logo=github)](https://)
[![Made with Python](https://img.shields.io/badge/Python->=3.8-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![GitHub tag](https://img.shields.io/github/tag/TOMG-A/DijkstrasAlgorithm?include_prereleases=&sort=semver)](https://github.com/TOMG-A/DijkstrasAlgorithm/releases/)


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

Released under [MIT](/LICENSE) by [@TOMG-A](https://github.com/TOMG-A).
