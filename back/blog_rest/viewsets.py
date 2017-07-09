from rest_framework import viewsets
from rest_framework.views import APIView
from blog_rest.serializers import CitySerializer, PostSerializer, RegionSerializer, ImageSerializer
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
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        print(self.request.data.get('image'))
        serializer.save(image=self.request.data.get('image'))

# class ImageViewSet(viewsets.ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     file = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
#     serializer = UploadedBase64ImageSerializer(data={'created': datetime.now(), 'file': file})
#     parser_classes = (FormParser, MultiPartParser)
#
#     def perform_create(self, serializer):
#         file_obj = self.request.FILES
#         print(file_obj)
