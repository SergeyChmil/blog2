from rest_framework import serializers
from blog.models import City, Post, Region, Image


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('pk', 'name')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('pk', 'name', 'region')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'name', 'body', 'city', 'publication_date', 'image')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('pk', 'name', 'post', 'image')

    image = serializers.ImageField(max_length=None, use_url=True)


