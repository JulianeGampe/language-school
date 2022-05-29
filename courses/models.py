from django.db import models


STATUS = ((0, "Bookable"), (1, "Booking closed"))


class Level(models.Model):
    name = models.CharField(max_length=254)
    friendlyname = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendlyname(self):
        return self.friendlyname


class Format(models.Model):
    name = models.CharField(max_length=254)
    friendlyname = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendlyname(self):
        return self.friendlyname


class Course(models.Model):
    name = models.CharField(max_length=254)
    level = models.ForeignKey(
        'Level', null=True, blank=True, on_delete=models.SET_NULL
    )
    format = models.ForeignKey(
        'Format', null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    startdate = models.DateField()
    weekday = models.CharField(max_length=254)
    time = models.TimeField()
    duration = models.CharField(max_length=254)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name
