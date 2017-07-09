from django.db import models
from django.conf import settings
import uuid

# from blog_rest.serializers import Base64ImageField

DEFAULT_REGION_ID = 1
DEFAULT_CITY_ID = 4


def scramble_uploaded_image_name(instance, filename):
    extension = filename.split('.')[-1]
    directory = instance.user.username
    return '{}/{}.{}'.format(directory, uuid.uuid4(), extension)


class Region(models.Model, ):
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class City(models.Model, ):
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    name = models.CharField(max_length=30, unique=True)
    region = models.ForeignKey(Region, default=DEFAULT_REGION_ID)

    def __str__(self):
        return self.name


class Post(models.Model, ):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    publication_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=40, unique_for_date="publication_date", default='New post')
    body = models.TextField()
    city = models.ForeignKey(City, default=DEFAULT_CITY_ID)
    images = models.CharField(max_length=999992, blank=True, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length=40, default='New post')
    post = models.IntegerField(default=0)
    image = models.ImageField('Uploaded Image', null=True, blank=True, upload_to=scramble_uploaded_image_name)
    # image = Base64ImageField(max_length=None, use_url=True)

    def __str__(self):
        return self.name
