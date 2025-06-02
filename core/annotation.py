def annotate_stream(stream, annotations):
    """
    Массово добавляет аннотации к потоку узлов.
    :param stream: список STNNode
    :param annotations: список строк (аннотаций)
    """
    if len(stream) != len(annotations):
        raise ValueError(f"Длины потока ({len(stream)}) и аннотаций ({len(annotations)}) не совпадают")
    for i, (node, annotation) in enumerate(zip(stream, annotations)):
        if not hasattr(node, 'annotation'):
            raise TypeError(f"Элемент с индексом {i} не поддерживает аннотации")
        node.annotation = annotation

