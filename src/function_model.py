import numpy as np

class IdealFunction:
    def __init__(self, name, x_values, y_values):
        self.name = name
        self.x = x_values
        self.y = y_values

    def get_summary(self):
        return {
            "name": self.name,
            "mean": np.mean(self.y),
            "std": np.std(self.y),
            "min": np.min(self.y),
            "max": np.max(self.y)
        }

    def evaluate(self, x_query):
        if x_query in self.x.values:
            idx = self.x[self.x == x_query].index[0]
            return self.y.iloc[idx]
        return None

class FunctionManager:
    def __init__(self, df):
        self.functions = []
        self.x = df["x"]
        for col in df.columns[1:]:
            func = IdealFunction(col, self.x, df[col])
            self.functions.append(func)

    def get_all_summaries(self):
        return [func.get_summary() for func in self.functions]

    def find_high_variance_functions(self, threshold):
        return [func for func in self.functions if np.std(func.y) > threshold]
