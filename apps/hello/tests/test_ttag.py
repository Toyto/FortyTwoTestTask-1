import django.test as test
from django.core.urlresolvers import reverse


class TemplateTagTest(test.TestCase):
    fixtures = ['initial_data.json']

    def test_edit_link_template_tag(self):
        """ Test for edit link template tag"""
        response = self.client.get(reverse('index'))
        self.assertIn(
            b'<a href="/admin/hello/about_me/1/"' +
            b' style="margin-left: 80%;">(admin)</a>', response.content)
