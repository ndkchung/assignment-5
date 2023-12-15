# Example usage:
from src.rainfall_analysis.models import DataReader

csv_file_path = "/home/andyc/assignment-5/data/Rainfall_Data_LL.csv"
data_reader = DataReader(csv_file_path)

# Take user input for the subdivision and year
user_input_subdivision = input("Please provide a subdivision: ")
user_input_year = input("Please provide a year between 1901 to 2017: ")

# Plot average rainfall for the specified subdivision and year
data_reader.plot_rainfall_data(user_input_subdivision, user_input_year)