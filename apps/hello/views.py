from .models import About_me
from django.views.generic import TemplateView
import logging
logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['about_me'] = About_me.objects.get(pk=1)
        logger.info(self.request)
        logger.info(context)
        return context
