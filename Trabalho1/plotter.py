import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, points, control_points):
        self.points = points
        self.control_points = control_points

    def plot_points(self, title, size):
        plt.figure(figsize=(size[0] / 100, size[1] / 100))
        self._plot_data(size, self.points.T[0].A1, self.points.T[1].A1, 'dodgerblue')
        if len(self.control_points) > 0:
          self._plot_data(size, self.control_points.T[0].A1, self.control_points.T[1].A1, 'red')
        plt.title(title)
        plt.show()

    def _plot_data(self, size, x_data, y_data, color):
        width, height = size
        plt.scatter(x_data * width/2, y_data * height/2, color=color)