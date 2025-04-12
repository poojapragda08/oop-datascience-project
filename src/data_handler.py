import pandas as pd

class DataHandler:
    def __init__(self, db_engine):
        self.engine = db_engine

    def load_csv(self, file_path):
        self.df = pd.read_csv(file_path, delimiter="\t")  # FIXED: correct indentation
        return self.df

    def save_to_db(self, table_name):
        self.df.to_sql(table_name, self.engine, if_exists="replace", index=False)
