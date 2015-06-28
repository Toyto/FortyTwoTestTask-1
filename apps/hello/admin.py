from django.contrib import admin
from .models import About_me


class AdminAbout_me(admin.ModelAdmin):
    list_display = ('name', 'surname', 'bio', 'contacts')

admin.site.register(About_me, AdminAbout_me)
