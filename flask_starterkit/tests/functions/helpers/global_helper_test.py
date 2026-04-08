"""Tests for global helper functions."""
import unittest

from flask_starterkit.main.helpers import super_complex_function


class TestAuthRoutes(unittest.TestCase):
    """Test cases for the super_complex_function helper."""

    def test_super_complex_function(self):
        """Test that super_complex_function returns the expected greeting."""
        self.assertEqual(super_complex_function("World !"), "Hello World !")


if __name__ == '__main__':
    unittest.main()
