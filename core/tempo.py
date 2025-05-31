def SPEED(node, factor):
    """
    Изменяет tempo узла.
    :param node: экземпляр STNNode
    :param factor: float (>1 ускоряет, <1 замедляет)
    """
    return node.speed(factor)
