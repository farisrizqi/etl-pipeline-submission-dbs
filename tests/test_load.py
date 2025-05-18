import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pandas as pd
from utils.load import save_to_csv

class TestLoad(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame([{
            "title": "Test Shirt",
            "price": 400000,
            "rating": 4.0,
            "colors": 2,
            "size": "L",
            "gender": "Men",
            "timestamp": "2025-05-18 10:00:00"
        }])

    def test_save_to_csv_runs(self):
        try:
            save_to_csv(self.df, "test_output.csv")
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
