import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from utils.extract import scrape_page

class TestExtract(unittest.TestCase):

    def test_scrape_page_not_empty(self):
        url = "https://fashion-studio.dicoding.dev/"
        result = scrape_page(url)
        self.assertGreater(len(result), 0, "Hasil scrape kosong, seharusnya ada data.")

    def test_scrape_page_data_format(self):
        url = "https://fashion-studio.dicoding.dev/"
        result = scrape_page(url)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], dict)

        keys = ["title", "price", "rating", "colors", "size", "gender"]
        for key in keys:
            self.assertIn(key, result[0])

if __name__ == '__main__':
    unittest.main()
