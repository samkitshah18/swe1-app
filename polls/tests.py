from django.test import TestCase


# Create your tests here.
class AssertTests(TestCase):
    def test_dummy(self):
        self.assertIs(False, False)
