from django.db import models

from django.utils.html import mark_safe
from django.core.exceptions import ValidationError


# Create your models here.
class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__ (self):
        return self.first_name

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="120px" />'%(self.image.url))
    image_tag.short_description = 'Image'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    details=models.TextField()
    date=models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.title

    def clean(self):
        if  len(self.title) > 10:
            raise ValidationError(
                {'title': "Title should have at least 10 letters"})
