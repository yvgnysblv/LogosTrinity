# stnlib/filters.py
from .node import STNNode

def active_nodes(node: STNNode) -> bool:
    """Фильтр для активных узлов (state != 0)"""
    return node.state != 0

def fast_nodes(node: STNNode, threshold=1.0) -> bool:
    """Фильтр для узлов со скоростью выше порога"""
    return node.tempo > threshold