iimport requests
import unittest


class TestATGWorldWebsite(unittest.TestCase):

    def test_website_loading(self):
        # Set up the URL to connect
        url = "https://jenkins.rushikesh.me/"
        print(f"Connecting to {url}...")

        # Connect to the website
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content[:80]}...")

        # Verify the response code
        self.assertEqual(response.status_code, 200)
        print("Website loaded successfully!")

if __name__ == '__main__':
    unittest.main()
