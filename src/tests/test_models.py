import os
import unittest
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from src.rainfall_analysis.models import DataReader

class TestDataAnalysisMethods(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            'SUBDIVISION': ['North', 'South', 'East'],
            'YEAR': [2000, 2001, 2002],
            'JAN': [10, 15, 20],
            'FEB': [5, 10, 15],
            'MAR': [8, 12, 18],
            'APR': [11, 7, 13],
            'MAY': [4, 12, 6],
            'JUN': [6, 18, 12],
            'JUL': [10, 9, 8],
            'AUG': [9, 7, 8],
            'SEP': [10, 10, 12],
            'OCT': [13, 9, 6],
            'NOV': [6, 5, 8],
            'DEC': [3, 12, 18]

        }
        self.sample_df = pd.DataFrame(data)
        self.sample_df.to_csv('test_data.csv', index=False)
        self.data_reader = DataReader('test_data.csv')

    def tearDown(self):
        # Clean up test files
        import os
        os.remove('test_data.csv')

    def test_read_file(self):
        df = self.data_reader.read_file()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue('SUBDIVISION' in df.columns)
        self.assertTrue('YEAR' in df.columns)
        self.assertEqual(len(df), 3)

    def test_plot_rainfall_data(self):
        # Test plotting with existing subdivision and year
        self.data_reader.plot_rainfall_data('North', 2000)
        # Assertions to check if the plot is generated
        self.assertTrue(plt.gcf())
        self.assertTrue(os.path.exists("plot.png"))

        # Test plotting with non-existing subdivision and year
        with self.assertRaises(ValueError):
            self.data_reader.plot_rainfall_data('Invalid', 2001)

if __name__ == '__main__':
    unittest.main()

