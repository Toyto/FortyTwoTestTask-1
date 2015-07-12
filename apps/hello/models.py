from django.db import models


class About_me(models.Model):
    name = models.CharField(max_length=33, default='name')
    surname = models.CharField(max_length=33, default='surname')
    bio = models.CharField(max_length=500, default='bio')
    contacts = models.CharField(max_length=150, default='contacts')
    birth_date = models.DateField('birth date')
    email = models.EmailField()
    jabber = models.CharField(max_length=50, default='id')
    skype = models.CharField(max_length=33, default='skype')
    photo = models.ImageField(upload_to='photos', blank=True)

    def __str__(self):
        return self.name


class AllRequests(models.Model):
    choice = [(i, i) for i in range(1, 11)]

    date_time = models.DateTimeField(auto_now=True, auto_now_add=True,
                                     blank=True)
    request_method = models.CharField(max_length=10)
    path = models.CharField(max_length=100)
    server_protocol = models.CharField(max_length=10)
    status_code = models.IntegerField(max_length=3)
    content_len = models.IntegerField(max_length=100)
    priority = models.IntegerField(default=1, choices=choice, blank=True)

    class Meta:
        ordering = ['date_time']


class ChangesLog(models.Model):
    model = models.CharField(max_length=35)
    operation = models.CharField(max_length=20)
    date_time = models.DateTimeField(auto_now=True, auto_now_add=True)
