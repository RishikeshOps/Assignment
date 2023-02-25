import requests
import unittest

class TestWebsiteLoading(unittest.TestCase):
    
    def test_website_loading(self):
        # Set up the URL to connect
        url = "https://atg.world/"
        
        # Connect to the website
        response = requests.get(url)
        
        # Verify the response code
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
