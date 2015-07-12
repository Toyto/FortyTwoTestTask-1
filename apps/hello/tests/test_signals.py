from django.test import TestCase
from apps.hello.models import ChangesLog, About_me


class EntryChangesLogTest(TestCase):
    fixtures = ['initial_data.json']

    def test_object_create(self):
        """Test create operation"""
        ChangesLog.objects.all().delete()
        person = About_me.objects.get(pk=1)
        self.assertEqual(person.name, 'Andrew')
        self.assertEqual(ChangesLog.objects.all().count(), 0)
        About_me.objects.create(name='Vasya',
                                surname='Vasya',
                                birth_date='1980-12-11',
                                bio='bio',
                                email='vas@gmail.com',
                                jabber='007',
                                skype='skype',
                                contacts='qwe')
        self.assertEqual(About_me.objects.all().count(), 2)
        self.assertEqual(ChangesLog.objects.get(pk=1).operation, 'create')
        self.assertEqual(ChangesLog.objects.all().count(), 1)

    def test_object_update(self):
        """Test update operation"""
        ChangesLog.objects.all().delete()
        person = About_me.objects.get(pk=1)
        person.name = 'John'
        person.save()
        self.assertEqual(person.name, 'John')
        self.assertEqual(ChangesLog.objects.get(pk=1).operation, 'update')
        self.assertEqual(ChangesLog.objects.all().count(), 1)

    def test_object_delete(self):
        """Test delete operation"""
        ChangesLog.objects.all().delete()
        About_me.objects.all().delete()
        self.assertEqual(ChangesLog.objects.get(pk=1).operation, 'delete')
        self.assertEqual(ChangesLog.objects.all().count(), 1)
