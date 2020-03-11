from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define test that we'll run against our product models
    """

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')