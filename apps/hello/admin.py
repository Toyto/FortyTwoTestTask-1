from django.contrib import admin
from .models import About_me, AllRequests, ChangesLog


class AdminAbout_me(admin.ModelAdmin):
    list_display = ('name', 'surname', 'bio', 'contacts')


class RequestsAdmin(admin.ModelAdmin):
    list_display = ('request_method', 'date_time', 'priority', 'path',
                    'server_protocol', 'status_code', 'content_len')


class ChangesLogAdmin(admin.ModelAdmin):
    list_display = ('model', 'operation', 'date_time')
    list_filter = ('model',)

admin.site.register(About_me, AdminAbout_me)
admin.site.register(AllRequests, RequestsAdmin)
admin.site.register(ChangesLog, ChangesLogAdmin)
