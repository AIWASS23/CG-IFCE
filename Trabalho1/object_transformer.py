import math
import numpy as np
from transformer import Transformer
from transformer_matrix import TransformationMatrixGenerator


class ObjectTransformer:
    def __init__(self, objects):
        self.objects = objects

    def generate_quadrant_transformed_objects(self):
        size = len(self.objects)
        step = math.floor(math.log2(size))
        quadrants = np.array([(1, 1), (-1, 1), (-1, -1), (1, -1)]) * (1/step)

        matrices = []
        for dx, dy in quadrants:
            for i in range(2):
                for j in range(step):
                    matrices.append(TransformationMatrixGenerator.generate(dx, dy, i, j))
                    if len(matrices) >= len(self.objects):
                        return Transformer.apply(self.objects, matrices)
            
        return Transformer.apply(self.objects, matrices)