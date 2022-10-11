from django_filters import rest_framework as filters

from test3.models import Laptop


class LaptopFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='exact', label='Имя')
    age = filters.NumberFilter(field_name='age', lookup_expr='contains', label='Возрост')

    class Meta:
        model = Laptop
        fields=('name', 'age')
