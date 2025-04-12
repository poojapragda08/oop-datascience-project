from data_handler import DataHandler
from function_model import IdealFunction, FunctionManager
from visualizer import Visualizer
from sqlalchemy import create_engine
import os

db_path = "data/ideal_functions.db"
csv_path = "data/ideal.csv"
engine = create_engine(f'sqlite:///{db_path}')

# Create database if it doesn't exist
handler = DataHandler(engine)
if not os.path.exists(db_path):
    print("Creating database...")
    df = handler.load_csv(csv_path)
    df.columns = [col.strip().lower() for col in df.columns]  # Clean col names
    handler.df = df  # set clean df in handler
    handler.save_to_db("ideal_functions")
else:
    print("Loading from existing database...")

# Load and clean DataFrame
df = handler.load_csv(csv_path)
df.columns = [col.strip().lower() for col in df.columns]
print("DataFrame Columns:", df.columns.tolist())  # debug print

# Continue as before
manager = FunctionManager(df)
high_var_funcs = manager.find_high_variance_functions(10)
visualizer = Visualizer(high_var_funcs[:4])
visualizer.plot_static()
