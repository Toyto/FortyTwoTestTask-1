from apps.hello.models import AllRequests
from django.core.urlresolvers import reverse


class RequestMiddleware():

    def process_response(self, request, response):
        if request.path != reverse('requests'):
            AllRequests.objects.create(
                request_method=request.META['REQUEST_METHOD'],
                path=request.path,
                server_protocol=request.META['SERVER_PROTOCOL'],
                status_code=response.status_code,
                content_len=len(response.content))
        else:
            pass
        return response
