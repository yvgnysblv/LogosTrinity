from core.node import STNNode
from core.stream_ops import map_sense, reduce_sense

def test_map_reduce():
    nodes = [STNNode(state=0) for _ in range(3)]
    map_sense(nodes, lambda n: setattr(n, "state", 1))
    assert all(n.state == 1 for n in nodes)
    total = reduce_sense(nodes, lambda acc, n: acc + n.state, 0)
    assert total == 3
