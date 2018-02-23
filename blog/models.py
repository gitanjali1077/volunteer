from __future__ import unicode_literals
from django.db import models
# Create your models here.
from django.db.models import permalink

class vacancy(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    no_of_vacancies = models.CharField(max_length=100)
    last_date = models.DateField(db_index=True)
    posted_on = models.DateTimeField(db_index=True, auto_now_add=True)
    
    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return self.title
