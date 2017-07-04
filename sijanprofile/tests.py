from django.test import TestCase

# Create your tests here.
from sijanprofile.views import TestMath


class MathTest(TestCase):
    def test_addition(self):
        # Make test fail
        self.assertEqual(TestMath.add_numbers(3, 4), 8)
