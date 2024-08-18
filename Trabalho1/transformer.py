from coord_transfomer import HomogeneousCoordinateTransformer


class Transformer:
    #Aplicar matrizes de transformação * matriz de coordenada homogenea
    @staticmethod
    def apply(objects, matrices):
        transformed_objects = []
        for obj, matrix in zip(objects, matrices):
            if isinstance(obj, list) and len(obj) >= 2:
                transformed = [
                    HomogeneousCoordinateTransformer(matrix @ HomogeneousCoordinateTransformer(sub_obj).to_homogeneous()).to_cartesian()
                    for sub_obj in obj
                ]
            else:
                transformed = HomogeneousCoordinateTransformer(matrix @ HomogeneousCoordinateTransformer(obj).to_homogeneous()).to_cartesian()
            transformed_objects.append(transformed)
        return transformed_objects