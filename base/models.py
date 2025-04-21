from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    type = models.ForeignKey('NoteType',on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)


class NoteType(models.Model):
    title = models.CharField(max_length=300)