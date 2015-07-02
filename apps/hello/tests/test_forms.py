from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import About_me


class FormTest(TestCase):
    fixtures = ['initial_data.json']

    def test_template_show(self):
        """ Test template """
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_edit_form_data(self):
        """ Test register page data """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        data = About_me.objects.get(pk=1)
        self.assertContains(response, data.name, 1)
        self.assertContains(response, data.surname, 1)
        self.assertContains(response, data.birth_date, 1)
        self.assertContains(response, data.bio, 1)
        self.assertContains(response, data.email, 1)
        self.assertContains(response, data.jabber, 1)
        self.assertContains(response, data.skype, 1)
        self.assertContains(response, data.contacts, 1)
