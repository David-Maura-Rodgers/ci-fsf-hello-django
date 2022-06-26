# python3 manage.py test
# pip3 install 'django<4'
# python3 manage.py runserver
# pip3 install coverage
# coverage run --source=todo manage.py test
# coverage report
# coverage html
# python3 -m http.server
from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
