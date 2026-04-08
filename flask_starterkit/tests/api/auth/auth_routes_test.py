"""Tests for auth API routes."""
import unittest

from dotenv import load_dotenv

from flask_starterkit.main.config import create_app


class TestAuthRoutes(unittest.TestCase):
    """Test cases for the auth routes blueprint."""

    def setUp(self) -> None:
        load_dotenv()
        self.client = create_app().test_client()

    def test_auth_global_endpoint(self):
        """Test that the auth global endpoint returns the expected response."""
        try:
            auth_endpoint_request = self.client.get('/api/auth/')
            self.assertDictEqual(auth_endpoint_request.json, {
                "message": "Welcome to your awesome auth endpoint", "success": True})
        except ValueError as exc:
            raise SystemExit(ValueError) from exc


if __name__ == '__main__':
    unittest.main()
