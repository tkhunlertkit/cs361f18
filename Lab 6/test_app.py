import unittest
from app import App

class TestApp(unittest.TestCase):
    def test_login(self):
        # assume username is in the database with password of password
        a = App()
        result = a.command("login username password")
        self.assertEqual("username logged in", result)