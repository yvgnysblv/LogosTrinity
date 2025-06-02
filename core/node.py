# stnlib/node.py
import copy

VALID_STATES = {-1, 0, 1}

class STNNode:
    def __init__(self, state=0, meta=None, tempo=1.0, annotation=None):
        if state not in VALID_STATES:
            raise ValueError(f"state должен быть -1, 0 или 1, а не {state}")
        if not isinstance(tempo, (int, float)) or tempo < 0:
            raise ValueError(f"tempo должен быть неотрицательным числом, а не {tempo}")
        if annotation is not None and not isinstance(annotation, str):
            raise TypeError("annotation должна быть строкой или None")
        self.state = state
        self.meta = meta
        self.tempo = tempo
        self.annotation = annotation

    def speed(self, factor):
        if not isinstance(factor, (int, float)) or factor <= 0:
            raise ValueError("factor должен быть положительным числом")
        self.tempo *= factor
        return self.tempo

    def clone(self):
        return copy.deepcopy(self)

    def to_dict(self):
        return {
            'state': self.state,
            'meta': self.meta,
            'tempo': self.tempo,
            'annotation': self.annotation,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            state=d.get('state', 0),
            meta=d.get('meta'),
            tempo=d.get('tempo', 1.0),
            annotation=d.get('annotation')
        )

    def set_state(self, new_state):
        if new_state not in VALID_STATES:
            raise ValueError("state должен быть -1, 0 или 1")
        self.state = new_state

    def annotate(self, text):
        if text is not None and not isinstance(text, str):
            raise TypeError("annotation должна быть строкой или None")
        self.annotation = text

    def __eq__(self, other):
        if not isinstance(other, STNNode):
            return False
        return (self.state == other.state and
                self.meta == other.meta and
                self.tempo == other.tempo and
                self.annotation == other.annotation)

    def __repr__(self):
        return f"<STNNode state={self.state}, tempo={self.tempo}, annotation='{self.annotation}'>"