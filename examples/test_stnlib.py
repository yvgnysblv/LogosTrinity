import pytest
from stnlib import STNNode, map_sense, reduce_sense, StreamPipeline

def test_node_creation():
    node = STNNode(state=1, meta="test", tempo=2.5)
    assert node.state == 1
    assert node.meta == "test"
    assert node.tempo == 2.5

def test_map_reduce():
    nodes = [STNNode(state=1), STNNode(state=-1)]
    mapped = map_sense(nodes, lambda n: n.state)
    total = reduce_sense(mapped, lambda a, b: a + b, 0)
    assert total == 0

def test_pipeline():
    nodes = [STNNode(state=1), STNNode(state=-1), STNNode(state=0)]
    result = (
        StreamPipeline.of(nodes)
        .map(lambda n: n.state)
        .filter(lambda s: s != 0)
        .reduce(lambda a, b: a + b, 0)
    )
    assert result == 0