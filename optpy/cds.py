from algorithms import Algorithms


class CDS(Algorithms):
    def __init__(self, nodes=None):
        description = "blabla"
        super().__init__("CDS", description)
        self.nodes = nodes
        self.n_nodes = 0
        if nodes is not None:
            self.n_nodes = len(self.nodes.shape[0])
