from tokenize import group
from unicodedata import name
from .models import settings
from .models import *
from django.db.models.signals import post_save
from django.contrib.auth.models import Group

def Account_Create(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='a_encargado')
        instance.groups.add(group)
post_save.connect(Account_Create,sender=settings.AUTH_USER_MODEL)