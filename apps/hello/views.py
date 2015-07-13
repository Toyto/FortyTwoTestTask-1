from django.views.generic import TemplateView, FormView
from django.http import HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .util import JsonResponse
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
            path=reverse('requests'))[:10]
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

    def get_initial(self):
        super(CreateAuthView, self).get_initial()
        context = self.get_context_data()
        data = context['data']
        return {'name': data.name,
                'surname': data.surname,
                'bio': data.bio,
                'contacts': data.contacts,
                'birth_date': data.birth_date,
                'email': data.email,
                'jabber': data.jabber,
                'skype': data.skype,
                'photo': data.photo
                }

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        contacts = About_me.objects.last()
        form = AuthorForm(request.POST, request.FILES, instance=contacts)
        if form.is_valid():
            form.save()
            return JsonResponse({'data': {
                'name': contacts.name,
                'surname': contacts.surname,
                'bio': contacts.bio,
                'contacts': contacts.contacts,
                'birth_date': str(contacts.birth_date),
                'email': contacts.email,
                'jabber': contacts.jabber,
                'skype': contacts.skype,
                'photo': contacts.photo.url
            }
            })
        else:
            return HttpResponseBadRequest()
