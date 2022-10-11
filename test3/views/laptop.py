from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


from test3.models import Laptop
from test3.serializers import LaptopCreateSerializer
from test3.filters import LaptopFilter


class LaptopViewSet(ModelViewSet):
        serializers_class = LaptopCreateSerializer
        permission_classes = [IsAuthenticated]
        queryset = Laptop.objects.all()
        filter_backends = (DjangoFilterBackend,)
        filterset_class=LaptopFilter



        def get_serializer_class(self):
            serializer_class = LaptopCreateSerializer

            if self.action == 'create':
                serializer_class = LaptopCreateSerializer
            elif self.action == 'update':
                serializer_class = LaptopCreateSerializer
        #
            return serializer_class


