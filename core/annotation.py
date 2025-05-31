def annotate_stream(stream, annotations):
    """
    Массово добавляет аннотации к потоку узлов.
    :param stream: список STNNode
    :param annotations: список строк (аннотаций)
    """
    for node, annotation in zip(stream, annotations):
        node.annotation = annotation
