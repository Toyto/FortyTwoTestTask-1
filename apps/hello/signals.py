from apps.hello.models import ChangesLog
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save)  # NOQA
def post_save_signal(sender, created, **kwargs):
    if created and sender.__name__ != 'ChangesLog':
        ChangesLog.objects.create(
            model=sender.__name__, operation='create'
        )
    elif not created and sender.__name__ != 'ChangesLog':
        ChangesLog.objects.create(
            model=sender.__name__, operation='update'
        )


@receiver(post_delete)  # NOQA
def post_delete_signal(sender, **kwargs):
    if sender.__name__ != 'ChangesLog':
        ChangesLog.objects.create(
            model=sender.__name__, operation='delete'
        )
