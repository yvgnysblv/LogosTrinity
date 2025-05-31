from core.node import STNNode
from core.tempo import SPEED

def test_speed():
    n = STNNode()
    SPEED(n, 2)
    assert n.tempo == 2.0
    SPEED(n, 0.5)
    assert n.tempo == 1.0
