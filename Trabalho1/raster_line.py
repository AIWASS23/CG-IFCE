import numpy as np

def rasterizar_linha(pontos, num_fragments = 75):
    if len(pontos) > 2:
        results_divided = [rasterizar_linha(
            np.concatenate((pontos[i], pontos[i+1])), num_fragments)
                           for i in range(len(pontos)-1)]
        return np.concatenate(results_divided)
    else:
        dx = pontos[1, 0] - pontos[0, 0]
        dy = pontos[1, 1] - pontos[0, 1]
        increments = np.array([dx / num_fragments, dy / num_fragments])
        fragmentos = [pontos[0] + i * increments for i in range(num_fragments + 1)]
        return np.concatenate(fragmentos)