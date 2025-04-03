import unittest
from game import generate_number

class TestGuessTheNumberGame(unittest.TestCase):

    def test_generate_number(self):
        # Test that the number is between 1 and 100
        number = generate_number()
        self.assertGreaterEqual(number, 1)
        self.assertLessEqual(number, 100)

if __name__ == "__main__":
    unittest.main()
