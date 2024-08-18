import numpy as np
from normalizer import Normalizer
from object_transformer import ObjectTransformer

class Raster:
    def __init__(self, points):
        self.points = points
        self.points_normalized = [self._normalize_point(sublist) for sublist in self.points]

    @staticmethod
    def _normalize_point(sublist):
        if isinstance(sublist, list):
            return list(map(Normalizer.normalize, sublist))
        return Normalizer.normalize(sublist)

    def rasterize(self, commands):
        points_transformed = self._transform_points()
        rasterized_points = self._apply_commands(commands, points_transformed)
        return self._stack_points(points_transformed), np.vstack(rasterized_points)

    def rasterize_clip(self, clip_window, clip_command, commands):
        points_transformed = self._transform_points()
        clip_points = self._apply_clip_commands(clip_command, points_transformed, clip_window)
        rasterized_points = self._apply_commands(commands, clip_points, check_empty=True)
        return clip_points, np.vstack(rasterized_points)

    def _transform_points(self):
        return ObjectTransformer(self.points_normalized).generate_quadrant_transformed_objects()

    def _apply_commands(self, commands, points, check_empty=False):
        rasterized_points = []
        for func, (interval, position) in commands.items():
            for i in interval:
                if check_empty and self._is_empty(points[i]):
                    continue
                args = [points[i]] if not isinstance(points[i], list) else points[i]
                result = func(*args)
                result = result[position] if isinstance(result, tuple) else result
                if not self._is_empty(result):
                    rasterized_points.append(result)
        return rasterized_points

    def _apply_clip_commands(self, clip_command, points_transformed, clip_window):
        clip_points = []
        for func_clip, interval in clip_command.items():
            for i in interval:
                args = [points_transformed[i]] if not isinstance(points_transformed[i], list) else points_transformed[i]
                args.append(clip_window)
                result = func_clip(*args)
                clip_points.append(result)
        return clip_points

    @staticmethod
    def _is_empty(result):
        return (isinstance(result, np.matrix) and (result.shape[0] == 0 or result.shape[1] == 0)) or \
               (isinstance(result, list) and len(result) == 0)

    @staticmethod
    def _stack_points(points):
        return np.vstack([x[0] if isinstance(x, list) and len(x) >= 2 else x for x in points])
