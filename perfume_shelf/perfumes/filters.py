import django_filters
from django.db.models import Q

from .models import Perfume


class PerfumeFilter(django_filters.FilterSet):
    name_or_brand = django_filters.CharFilter(
        method='name_or_brand_search',
        label='Название парфюма или бренд')
    notes = django_filters.CharFilter(
        method='notes_search',
        label='Присутствуют ноты')

    class Meta:
        model = Perfume
        fields = [
            'name_or_brand',
            'gender',
            'perfume_group',
            'season',
            'usage',
            'notes',
            'have_it',
            'had_it',
            'want_it',
            'test_it'
        ]

    def name_or_brand_search(self, queryset, name, value):
        queryset = queryset.filter(Q(perfume_name__icontains=value) |
                                   Q(brand__icontains=value))
        return queryset

    def notes_search(self, queryset, name, value):
        queryset = queryset.filter(Q(top_notes__icontains=value) |
                                   Q(middle_notes__icontains=value) |
                                   Q(base_notes__icontains=value))
        return queryset
