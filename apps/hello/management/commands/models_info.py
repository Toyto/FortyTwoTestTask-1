import sys
from django.core.management.base import NoArgsCommand
from django.db import models


class Command(NoArgsCommand):
    help = 'Prints all project models and the count of objects in every model'

    def handle(self, **options):
        for app in models.get_apps():
            for model in models.get_models(app):
                sys.stderr.write(
                    'error: %s: objects: %d\n' % (
                        model.__name__, model.objects.count())
                )
