from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    lectures_count = models.IntegerField()
