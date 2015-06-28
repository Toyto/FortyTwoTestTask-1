from django.db import models


def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])


class About_me(models.Model):
    name = models.CharField(max_length=33, default='name')
    surname = models.CharField(max_length=33, default='surname')
    bio = models.CharField(max_length=500, default='bio')
    contacts = models.CharField(max_length=150, default='contacts')
    birth_date = models.DateField('birth date')
    email = models.EmailField()
    jabber = models.CharField(max_length=50, default='id')
    skype = models.CharField(max_length=33, default='skype')
    photo = models.ImageField(upload_to=content_file_name, blank=True)

    def __str__(self):
        return self.name
