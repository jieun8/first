from django.db import models
from django.utils import timezone

class User(models.Model):
    user_name = models.CharField(max_length=10)
    user_level = models.IntegerField(default=1)

    def __str__(self):
        return self.user_name
        #return "{}/{}/{}".format(self.id, self.user_name, self.user_level)


class Pockemon(models.Model):
    #catched_by = models.ForeignKey(User)
    #catched_when = models.DateTimeField(default=timezone.now)
    #lnglat = models.CharField(max_length=50, blank=True)
    po_name = models.CharField(max_length=10)
    po_level = models.IntegerField(default=1)

    def __str__(self):
        return self.po_name

    #def lat(self):
    #    return self.catched_where.split(',')[1]

    #def lng(self):
    #    return self.catched_where.split(',')[0]


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Capture(models.Model):
    user = models.ForeignKey(User)
    pockemon = models.ForeignKey(Pockemon)
    region = models.ForeignKey(Region)
    when = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}가 {}에서 {}에 {}를 포획!".format(self.user, self.region, self.when, self.pockemon)