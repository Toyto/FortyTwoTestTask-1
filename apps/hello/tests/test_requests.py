from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import AllRequests


class MiddlewareTests(TestCase):
    fixtures = ['initial_data.json']

    def test_middleware_write(self):
        """ Checking existence requests """
        requests = AllRequests.objects.all()
        self.assertEqual(requests.count(), 0)
        self.client.get(reverse('index'))
        requests = AllRequests.objects.all()
        self.assertEqual(requests.count(), 1)
