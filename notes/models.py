import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200, default='')
    text = models.TextField()
    time = models.DateField(auto_now=True)
    passwd = models.CharField(max_length=30, default='')
    ref = models.UUIDField(editable=False, default=uuid.uuid4)

    def __str__(self):
        return self.title

    def link(self, type='view'):
        name = 'notes:%s' % type
        return reverse(name, args=(str(self.ref), ))
