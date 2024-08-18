import numpy as np

class HomogeneousCoordinateTransformer:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def to_homogeneous(self):
        return np.vstack((self.coordinates.T, np.ones(self.coordinates.T.shape[1])))

    def to_cartesian(self):
        return self.coordinates[:-1, :].T