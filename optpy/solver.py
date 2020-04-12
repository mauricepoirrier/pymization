import numpy as np
from cds import CDS


class Solver:
    """Main class of the package. Solves pre-defined optimization problems.
    """

    def __init__(self, model=None):
        self.model_name = model
        self.nodes = None
        self.instance = None

    def load_data_csv(self, path_file, skip_rows=0):
        np.genfromtxt(path_file, delimiter=",", skiprows=skip_rows)

    def run(self, model):
        if model is not None:
            self.model_name is None
        if self.model_name is None:
            raise RuntimeError("There wasn't any model defined")
        self._instance_by_name()
        self.instance.run()

    def _instance_by_name(self):
        if self.nodes is None:
            raise RuntimeError("First load the data using load_data_csv")
        instance_helper = {"CDS": CDS(self.nodes)}
        if self.model_name not in instance_helper:
            raise RuntimeError("Algorithm is not yet implemented")
        self.instance = instance_helper[self.model_name]
