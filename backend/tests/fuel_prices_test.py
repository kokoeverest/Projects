import unittest
from services.scrapers.fuel_prices_today import scrape_fuel_prices, FUELO_URL


class FuelPricesPageTest(unittest.TestCase):
    """This test validates the correct extraction of the fuel prices for today"""

    def test_getFuelPrices_returnDictWithPrices(self):
        # Arrange & Act
        prices, query = scrape_fuel_prices(FUELO_URL)
        
        # Assert
        self.assertIsInstance(prices, dict)
        self.assertIsInstance(query, list)        
        self.assertEqual(len(prices), 4)
        self.assertEqual(len(query), 4)