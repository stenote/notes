from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
