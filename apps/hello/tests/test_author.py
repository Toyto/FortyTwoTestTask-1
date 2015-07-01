from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import About_me


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

    def test_index_value_limit(self):
        """ Test index value limit """
        About_me.objects.create(name='Goro',
                                surname='Moro',
                                birth_date='1995-01-22',
                                bio='qwe',
                                email='s_brin@gmail.com',
                                jabber='123321',
                                skype='s_brin',
                                contacts='qwe')
        contacts = About_me.objects.all()
        self.assertEqual(contacts.count(), 4)
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Email:', 1)
        self.assertNotContains(response, 'Goro')

    def test_data_index(self):
        """ Test data on index """
        response = self.client.get(reverse('index'))
        contacts = About_me.objects.all()
        self.assertEqual(response.status_code, 200)
        contact = contacts[0]
        self.assertContains(response, contact.name, 1)
        self.assertContains(response, contact.surname, 1)
        self.assertContains(
            response,
            contact.birth_date.strftime('%B %d, %Y').replace('0', ''), 1
        )
        self.assertContains(response, contact.bio, 1)
        self.assertContains(response, contact.email, 1)
        self.assertContains(response, contact.jabber, 1)
        self.assertContains(response, contact.skype, 1)
        self.assertContains(response, contact.contacts, 1)
