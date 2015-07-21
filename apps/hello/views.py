from django.views.generic import TemplateView, FormView
from django.http import HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

from .util import JsonResponse
from apps.hello import signals  # NOQA
from .models import About_me, AllRequests
from .forms import AuthorForm

import logging
logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['data'] = About_me.objects.get(pk=1)
        logger.info(u'Landing page request %s', self.request)
        logger.debug(u'Landing page context %s', context)
        return context


class RequestView(TemplateView):
    template_name = 'requests.html'

    def get_context_data(self, **kwargs):
        context = super(RequestView, self).get_context_data(**kwargs)
        context['request_list'] = AllRequests.objects.exclude(
            path=reverse('requests')).order_by('-priority')[:10]
        context['new_requests'] = AllRequests.objects.exclude(
            path=reverse('requests'))
        logger.debug(u'Requests page context %s', context)
        return context


class CreateAuthView(FormView):
    template_name = 'register.html'
    form_class = AuthorForm

    def get_context_data(self, **kwargs):
        context = super(CreateAuthView, self).get_context_data(**kwargs)
        context['data'] = About_me.objects.get(pk=1)
        logger.info(u'Landing page request %s', self.request)
        logger.debug(u'Landing page context %s', context)
        return context

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        person = About_me.objects.last()
        form = AuthorForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
        else:
            return HttpResponseBadRequest()
        return redirect('index')


class PersonDataView(TemplateView):

    def get(self, request, *args, **kwargs):
        data = About_me.objects.get(pk=1)
        return JsonResponse({'name': data.name,
                             'surname': data.surname,
                             'bio': data.bio,
                             'contacts': data.contacts,
                             'birth_date': str(data.birth_date),
                             'email': data.email,
                             'jabber': data.jabber,
                             'skype': data.skype,
                             'photo': data.photo.url
                             })
