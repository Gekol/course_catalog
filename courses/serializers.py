from rest_framework import serializers
from . import models


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Course
        fields = ['title', 'date_start', 'date_end', 'lectures_count']


