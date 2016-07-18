from django.db import models
from django.utils import timezone

class User(models.Model):
    user_name = models.CharField(max_length=10)
    user_level = models.IntegerField(default=1)

    def __str__(self):
        return self.user_name


class Pockemon(models.Model):
    catched_by = models.ForeignKey(User)
    catched_when = models.DateTimeField(default=timezone.now)
    lnglat = models.CharField(max_length=50, blank=True)
    po_name = models.CharField(max_length=10)
    po_level = models.IntegerField(default=1)

    def __str__(self):
        return self.po_name

    def lat(self):
        return self.catched_where.split(',')[1]

    def lng(self):
        return self.catched_where.split(',')[0]