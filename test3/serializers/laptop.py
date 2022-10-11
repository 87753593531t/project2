from rest_framework import serializers


from test3.models import Laptop


class LaptopCreateSerializer(serializers.ModelSerializer):

     class Meta:
          model = Laptop
          fields = (
               'id',
               'name',
               'age'
          )






