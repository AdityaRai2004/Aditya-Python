import unittest
from unittest.mock import patch
from mymodule import calculate_square_root

class TestSquareRoot(unittest.TestCase):
    @patch('mymodule.math.sqrt')  # Mock the math.sqrt imported in mymodule
    def test_calculate_square_root(self, mock_sqrt):
        # Configure mock to return a fixed value
        mock_sqrt.return_value = 100
        
        # Test the function
        result = calculate_square_root(25)
        
        # Verify the result and mock usage
        self.assertEqual(result, 100)
        mock_sqrt.assert_called_once_with(25)

if __name__ == '__main__':
    unittest.main()
