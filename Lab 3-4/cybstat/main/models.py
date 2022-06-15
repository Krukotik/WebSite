from django.db import models


class CybdbModels(models.Model):
    title = models.CharField('name', max_length=100)
    data = models.TextField('data')

    def __str__(self):
        return self.title
