from core.node import STNNode
from core.annotation import annotate_stream

def test_annotate():
    nodes = [STNNode() for _ in range(2)]
    annotations = ["узел 1", "узел 2"]
    annotate_stream(nodes, annotations)
    assert nodes[0].annotation == "узел 1"
    assert nodes[1].annotation == "узел 2"
