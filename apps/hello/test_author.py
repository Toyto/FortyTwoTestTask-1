from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import About_me


# Ticket: 1, 2
class ViewsTest(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        About_me.objects.create(name='John', surname='Malkolm',
                                bio='bio', contacts='contacts',
                                birth_date='1995-05-05', email='asd@asd.asd',
                                jabber='id', skype='skype')
        About_me.objects.create(name='Bon', surname='Ronni',
                                bio='bio', contacts='contacts',
                                birth_date='1990-05-05', email='asd@asd.asd',
                                jabber='id', skype='skype')

    def test_author_exist(self):
        """ Checking existence author """
        author = About_me.objects.get(pk=1)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, author.name)

    def test_whom_will_show(self):
        """ Checking whom will show """
        must_be_first = About_me.objects.first()
        response = self.client.get(reverse('index'))
        self.assertContains(response, must_be_first.name)


# Create your tests here.
