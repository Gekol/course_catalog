import django_filters
from rest_framework import viewsets

from courses.models import Course


class EventFilter(django_filters.FilterSet):
    timestamp_gte = django_filters.DateFilter(name="date_start", lookup_expr='gte')

    class Meta:
        model = Course
        fields = ['date_start_gte']


class EventsView(viewsets.ReadOnlyModelViewSet):
    ...
    filter_class = EventFilter
