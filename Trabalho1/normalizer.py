import numpy as np

class Normalizer:
    @staticmethod
    def normalize(point):
        min_val, max_val = np.min(point), np.max(point)        
        return (point - min_val) / (max_val - min_val)