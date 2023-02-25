import requests
import unittest

class TestWebsiteLoading(unittest.TestCase):
    
    def test_website_loading(atg):
        # Set up the URL to connect
        url = "https://atg.world/"
        
        # Connect to the website
        response = requests.get(url)
        
        # Verify the response code
        atg.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
