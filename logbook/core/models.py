from __future__ import unicode_literals

from django.db import models
from django.db.models import permalink

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    url = models.URLField(max_length=200, blank=True)
    #posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('core.Category')
    date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, { 'slug' : self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_category', None, { 'slug': self.slug })
