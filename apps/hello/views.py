from django.views.generic import TemplateView, FormView
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

from .util import JsonResponse
from apps.hello import signals  # NOQA
from .models import About_me, AllRequests
from .forms import AuthorForm, RequestForm
import json

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


class RequestView(FormView):
    template_name = 'requests.html'
    form_class = RequestForm

    def get_context_data(self, **kwargs):
        context = super(RequestView, self).get_context_data(**kwargs)
        context['request_list'] = AllRequests.objects.all().order_by(
            '-priority')[:10]
        context['new_requests'] = AllRequests.objects.all()
        context['choices'] = range(1, 11)
        logger.debug(u'Requests page context %s', context)
        return context

    def post(self, request, *args, **kwargs):
        form = RequestForm(request.POST)
        requests_list = list(map(int, request.POST.getlist('id')))
        priority_list = list(map(int, request.POST.getlist('priority')))
        if form.is_valid():
            req = AllRequests.objects.filter(id__in=requests_list)
            for i, obj in enumerate(req):
                obj.priority = priority_list[i]
                obj.save()
            return redirect('requests')
        else:
            return HttpResponseBadRequest()


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
            errors_dict = {}
            if form.errors:
                for error in form.errors:
                    e = form.errors[error]
                    errors_dict[error] = e
            return HttpResponseBadRequest(json.dumps(errors_dict))
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
