from django.test import TestCase
from data.TA import TA

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_login(self):

        res = app.command("login user password")
        exp = "user logged in"
        self.assertEquals(res, exp)