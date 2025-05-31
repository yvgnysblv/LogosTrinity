from core.node import STNNode

def test_node_creation():
    n = STNNode(state=1, annotation="Тестовый узел")
    assert n.state == 1
    assert n.annotation == "Тестовый узел"
