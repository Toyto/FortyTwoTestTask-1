import os
from django.test import TestCase
from django.core.management import call_command


class CommandTests(TestCase):

    def test_command(self):
        """Test command models info"""

        fout = os.popen('python manage.py models_info').read()
        self.assertIn('', fout)
        call_command('models_info')
