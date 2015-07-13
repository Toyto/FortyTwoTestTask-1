from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import AllRequests


class AllRequestsTestCase(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client.get(reverse('index'))

    def test_priority_set(self):
        """ Test requests priority """
        self.assertEqual(AllRequests.objects.all().count(), 1)
        response = self.client.get(reverse('requests'))
        self.assertContains(response, 'Priority: 1', 1)
        req = AllRequests.objects.get(pk=1)
        req.priority = 3
        req.save()
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.context['request_list'][0].priority, 3)
        self.assertContains(response, 'Priority: 3', 1)
