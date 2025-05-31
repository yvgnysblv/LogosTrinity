class STNNode:
    def __init__(self, state=0, meta=None, tempo=1.0, annotation=None):
        self.state = state        # -1, 0, +1
        self.meta = meta          # любые смысловые данные
        self.tempo = tempo        # темп реализации (1.0 — стандарт)
        self.annotation = annotation  # естественно-языковой комментарий

    def speed(self, factor):
        self.tempo *= factor
        return self.tempo

    def __repr__(self):
        return (f"<STNNode state={self.state}, tempo={self.tempo}, "
                f"annotation={self.annotation}>")
