import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class DataReader:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def read_file(self):
        # Read the CSV file into a pandas DataFrame
        data = pd.read_csv(self.csv_file_path)
        return data

    def plot_rainfall_data(self, subdivision, year):
        # Read the data from the file
        data = self.read_file()

        # Convert both subdivision names to lowercase for case-insensitive comparison
        lowercased_subdivision = subdivision.lower()

        # Filter data based on subdivision and year
        filtered_data = data[(data["SUBDIVISION"].str.lower() == lowercased_subdivision) & (data["YEAR"] == int(year))]

        # Check if the filtered data is empty
        if filtered_data.empty:
            raise ValueError(f"There is no data found for '{subdivision}' in the year {year}.")


        # Plotting
        plt.figure(figsize=(10, 6))
        plt.title(f"Average Rainfall in {subdivision} - {year}")
        plt.xlabel("Month")
        plt.ylabel("Rainfall (mm)")

        # Iterate over rows and create a bar for each month
        for index, row in filtered_data.iterrows():
            months = data.columns[3:15]  # Assuming columns from 3rd onwards are months
            rainfall_values = row[months]
            plt.bar(months, rainfall_values)


        # Calculate the average rainfall for the specified year and subdivision
        average_rainfall = np.nanmean(filtered_data[months].values)

        # Displays the average rainfall for the specified year and subdivision
        plt.suptitle(f"Average Rainfall in {subdivision} for {year}: {average_rainfall:.2f} mm")

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')

        # Show the plot
        plt.show()
        # Save the plot to a PNG file
        plt.savefig("plot.png")

