from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import AllRequests


class MiddlewareTests(TestCase):
    fixtures = ['initial_data.json']

    def test_template(self):
        """ Test template """
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)

    def test_middleware_write(self):
        """ Checking requests existence """
        requests = AllRequests.objects.all()
        self.assertEqual(requests.count(), 0)
        self.client.get(reverse('index'))
        requests = AllRequests.objects.all()
        self.assertEqual(requests.count(), 1)

    def test_template_limit(self):
        """ Test requests limit """
        for i in range(10):
            self.client.get(reverse('index'))
            self.client.get(reverse('requests'))
        requests = AllRequests.objects.all()
        self.assertEqual(requests.count(), 20)
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.context['request_list'].count(), 10)
        req = AllRequests.objects.order_by('date_time')[:10]
        for i in range(10):
            self.assertEqual(
                response.context['request_list'].values_list(
                    'id', flat=True
                )[i],
                req.values_list('id', flat=True)[i]
            )
