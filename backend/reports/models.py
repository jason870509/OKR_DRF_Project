from django.db import models
from django.conf import settings
from django.db.models import Q
import os


def update_filename(instance, filename):
    path = 'files'
    format = str(instance.file_path).split('.pdf')[0] + '_1234' + '.pdf'
    return os.path.join(path, format)



class ReportQuerySet(models.QuerySet):
    def search(self, query, user=None):

        lookup = Q(title__icontains=query['title'])
        qs = self.filter(lookup)
        
        if query['author'] != "":
            lookup = Q(author=query['author'])
            qs = qs.filter(lookup)
        if query['category'] != "":
            lookup = Q(category=query['category'])
            qs = qs.filter(lookup)
        

        if user is not None:
            qs2 = self.filter(author=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ReportManager(models.Manager):
    def get_queryset(self, *arg, **kwargs):
        return ReportQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Report(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default=1)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file_path = models.FileField(upload_to=update_filename)
    create_at = models.DateTimeField(auto_now_add=True)

    objects = ReportManager()

    def __str__(self):
        return self.title