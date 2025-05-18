import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from utils.transform import transform_data
import pandas as pd

class TestTransform(unittest.TestCase):

    def setUp(self):
        # Data dummy mirip hasil scraping
        self.raw_data = [
            {
                "title": "Cool Shirt",
                "price": "$25.00",
                "rating": "4.5 out of 5 stars",
                "colors": "3 Colors",
                "size": "Size: M",
                "gender": "Gender: Men"
            },
            {
                "title": "Unknown Product",
                "price": "Price Unavailable",
                "rating": "No rating",
                "colors": "0 Colors",
                "size": "Size: -",
                "gender": "Gender: -"
            }
        ]

    def test_transform_result_structure(self):
        df = transform_data(self.raw_data)
        self.assertIsInstance(df, pd.DataFrame)
        expected_cols = ["title", "price", "rating", "colors", "size", "gender", "timestamp"]
        for col in expected_cols:
            self.assertIn(col, df.columns)

    def test_transform_price_conversion(self):
        df = transform_data([self.raw_data[0]])
        self.assertEqual(df.iloc[0]["price"], 25.00 * 16000)

    def test_transform_filters_unknown_product(self):
        df = transform_data(self.raw_data)
        self.assertNotIn("Unknown Product", df["title"].values)

if __name__ == '__main__':
    unittest.main()
