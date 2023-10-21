from django.db import models
from django.conf import settings
from django.db.models import Q


class ReportQuerySet(models.QuerySet):
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        qs = self.filter(lookup)

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
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file_path = models.FileField(upload_to='files/%Y/%m/%d')
    create_at = models.DateTimeField(auto_now_add=True)

    objects = ReportManager()

    def __str__(self):
        return self.title