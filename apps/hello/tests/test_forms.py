from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.forms import AuthorForm


class FormTest(TestCase):
    fixtures = ['initial_data.json']

    def test_template_show(self):
        """ Test template """
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_forms(self):
        """ Test form """
        self.client.login(username='admin', password='admin')
        form_data = {'name': 'Andrew', 'surname': 'Morn',
                     'birth_date': '1995-05-05',
                     'bio': 'bio', 'contacts': '1999119',
                     'email': 'asd@adsd.com',
                     'jabber': 'jid', 'skype': 'mysk'
                     }
        form = AuthorForm(data=form_data)
        self.assertEqual(form.is_valid(), True)
