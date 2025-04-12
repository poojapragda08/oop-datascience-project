import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, functions):
        self.functions = functions

    def plot_static(self):
        for func in self.functions:
            plt.plot(func.x, func.y, label=func.name)
        plt.legend()
        plt.title("Ideal Functions")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
