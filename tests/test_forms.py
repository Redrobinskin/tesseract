import unittest
from flask import Flask
from app.forms import MyForm

class TestForms(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()

    def test_form_validation(self):
        form = MyForm(self.client.post('/submit', data=dict(fieldname='data')))
        self.assertTrue(form.validate())

    def test_form_invalidation(self):
        form = MyForm(self.client.post('/submit', data=dict(fieldname='')))
        self.assertFalse(form.validate())

if __name__ == '__main__':
    unittest.main()