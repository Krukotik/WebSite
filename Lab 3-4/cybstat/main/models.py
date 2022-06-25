from django.db import models


class CybdbModels(models.Model):
    title = models.CharField('name', max_length=40)
    data = models.TextField('data')
    link = models.TextField('link', default="abc")
    img = models.ImageField(default='no_image.jpg', upload_to='product.image')

    def __str__(self):
        return self.title
