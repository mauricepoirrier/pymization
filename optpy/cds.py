from algorithms import Algorithms
import numpy as np
import logging


class CDS(Algorithms):
    def __init__(self, nodes=None):
        description = "blabla"
        super().__init__("CDS", description)
        self.nodes = nodes
        self.n_nodes = 0
        if nodes is not None:
            self.n_nodes = self.nodes.shape[0]
            self.n_jobs = self.nodes.shape[1]
        self.final_sequence = []
        self.objetive_function = np.Infinity
        self.first_mock_machine = []
        self.second_mock_machine = []
        self.first_nodes_set = []
        self.second_nodes_set = []

    def run(self):
        self.objetive_function = np.Infinity
        for i in range(self.n_nodes - 1):  # permutation numbers
            self.first_mock_machine, self.second_mock_machine = [], []
            self.first_node_set, self.second_node_set = [], []
            self._get_sets(i)
            self.first_node_set.sort()
            self.second_mock_machine.sort(reverse=True)
            self._previos_job(list(self.first_node_set + self.second_mock_machine))
        logging.info(
            f"Best seq: {self.final_sequence} | Objective function: {self.objetive_function}"
        )

    def _get_sets(self, permutation):
        for j in range(self.n_nodes):
            self.first_mock_machine.append(np.sum(self.nodes[j][: (permutation + 1)]))
            self.second_mock_machine.append(
                np.sum(self.nodes[j]) - np.sum(self.nodes[j][: (permutation + 1)])
            )
            if self.first_mock_machine[j] < self.second_mock_machine[j]:
                self.first_node_set.append(j)
            else:
                self.second_node_set.append(j)

    def _update_objective_function(self, time_job, seq):
        if self.objetive_function > time_job[-1]:
            self.objetive_function = time_job[-1]
            self.final_sequence = seq.copy()

    def _previos_job(self, node_sequence):
        time_previous_job = [0] * self.n_nodes
        time_previous_job[0] = self.nodes[node_sequence[0]][0]
        for i in range(1, self.n_nodes):
            time_previous_job[i] = (
                self.nodes[node_sequence[0]][i] + time_previous_job[i - 1]
            )
        time_job = [0] * self.n_nodes
        iterSecuencia = iter(node_sequence)
        next(iterSecuencia)
        for _, i in enumerate(iterSecuencia):
            time_job[0] = time_previous_job[0] + self.nodes[i][0]
            for j in range(1, self.n_nodes):
                if time_previous_job[j] >= time_job[j - 1]:
                    time_job[j] = self.nodes[i][j] + time_previous_job[j]
                else:
                    time_job[j] = self.nodes[i][j] + time_job[j - 1]
            time_previous_job = time_job.copy()
        self._update_objective_function(time_job, node_sequence)
