from rest_framework import viewsets
from rest_framework.views import APIView
from blog_rest.serializers import CitySerializer, PostSerializer, RegionSerializer, ImageSerializer
from rest_framework import generics
from blog.models import City, Post, Region, Image
from rest_framework.parsers import MultiPartParser, FormParser

class RegionViewSet(viewsets.ModelViewSet, APIView):
    queryset = Region.objects.order_by('pk')
    serializer_class = RegionSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.order_by('region', 'name')
    serializer_class = CitySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('publication_date')
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        region = self.request.query_params.get('region', None)
        if region is not None:
            queryset = queryset.filter(city__region=region)
        return queryset

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer