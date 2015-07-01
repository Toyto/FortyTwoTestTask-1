from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
register = template.Library()


def edit_link(obj):
    """{% edit_link object %}"""
    new_obj = ContentType.objects.get_for_model(obj.__class__)
    return reverse('admin:%s_%s_change' % (new_obj.app_label, new_obj.name), args=(obj.id,))

register.simple_tag(edit_link)