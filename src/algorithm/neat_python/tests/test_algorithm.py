from data.io_data_set import load_samples
from data.data_set import get_input_variables, get_target_variable
from algorithm.neat_python.algorithm import Neat
from algorithm.common.metric import RootMeanSquaredError, Accuracy
from algorithm.common.stopping_criterion import MaxGenerationsCriterion
import unittest


class TestNeat(unittest.TestCase):
    def setUp(self):
        self.training, self.validation, self.testing = load_samples('c_cancer', 0)
        self.neat = Neat(100, MaxGenerationsCriterion(200),
                         4, 1, 1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.01)

    def test_fit(self):
        X = get_input_variables(self.training).as_matrix()
        y = get_target_variable(self.training).as_matrix()
        self.neat.fit(X, y, Accuracy, verbose=True)
        self.assertTrue(expr=self.neat.champion)

if __name__ == '__main__':
    unittest.main()
