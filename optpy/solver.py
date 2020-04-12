import numpy as np


class Solver:
    """Main class of the package. Solves pre-defined optimization problems.
    """

    def __init__(self, model=None):
        self.model_name = model
        self.nodes = None

    def load_data_csv(self, path_file, skip_rows=0):
        np.genfromtxt(path_file, delimiter=",", skiprows=skip_rows)
