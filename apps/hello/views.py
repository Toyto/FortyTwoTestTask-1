from .models import About_me, AllRequests
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseBadRequest, HttpResponse
from .forms import AuthorForm
import logging
logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['data'] = About_me.objects.all()[:1]
        logger.info(u'Landing page request %s', self.request)
        logger.debug(u'Landing page context %s', context)
        return context


class RequestView(TemplateView):
    template_name = 'requests.html'

    def get_context_data(self, **kwargs):
        context = super(RequestView, self).get_context_data(**kwargs)
        context['request_list'] = AllRequests.objects.all()[:10]
        context['new_requests'] = AllRequests.objects.all()
        return context


class CreateAuthView(FormView):
    template_name = 'register.html'
    form_class = AuthorForm

    def post(self, request, *args, **kwargs):
        contacts = About_me.objects.last()
        form = AuthorForm(request.POST, request.FILES, instance=contacts)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')
        else:
            return HttpResponseBadRequest()
