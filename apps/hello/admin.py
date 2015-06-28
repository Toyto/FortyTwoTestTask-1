from django.contrib import admin
from .models import About_me, AllRequests


class AdminAbout_me(admin.ModelAdmin):
    list_display = ('name', 'surname', 'bio', 'contacts')


class RequestsAdmin(admin.ModelAdmin):
    list_display = ('request_method', 'date_time', 'path',
                    'server_protocol', 'status_code', 'content_len')


admin.site.register(About_me, AdminAbout_me)
admin.site.register(AllRequests, RequestsAdmin)
