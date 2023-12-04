# Dijkstra's Algorithm Implementation
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![Sample Project - View](https://img.shields.io/badge/Sample_Project-View-informational?logo=github)](https://)
[![Upload Python Package](https://github.com/TOMG-A/DijkstrasAlgorithm/actions/workflows/python-publish.yml/badge.svg)](https://github.com/TOMG-A/DijkstrasAlgorithm/actions/workflows/python-publish.yml)
[![Made with Python](https://img.shields.io/badge/Python->=3.8-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")

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


