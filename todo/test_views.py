# python3 manage.py test
from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):

    def test_this_thing_worse(self):
        self.assertEqual(1, 1)