import numpy as np


class TransformationMatrixGenerator:
    @staticmethod
    def generate(dx, dy, i, j):
        return np.array([
            [dx, 0, dx * j],
            [0, dy, dy * i],
            [0, 0, 1]
        ])