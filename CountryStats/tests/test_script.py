import unittest
import hashlib
from src.main_script import fetch_country_data, process_country_data

class TestCountryDataProcessing(unittest.TestCase):

    def test_fetch_country_data(self):
        url = "https://restcountries.com/v3.1/all"
        data = fetch_country_data(url)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0, "Data list should not be empty")

    def test_process_country_data(self):
        sample_data = [{
            'name': {'common': 'Test Country'},
            'languages': {'eng': 'English'}
        }]
        countries, languages, hashes, times = process_country_data(sample_data)
        self.assertEqual(countries[0], 'Test Country', "Country name should be 'Test Country'")
        self.assertEqual(languages[0], 'English', "Language should be 'English'")
        self.assertEqual(hashes[0], hashlib.sha1('English'.encode()).hexdigest(), "Hash should match the SHA1 of 'English'")
        self.assertIsInstance(times[0], float, "Time should be a float")

if __name__ == "__main__":
    unittest.main()
