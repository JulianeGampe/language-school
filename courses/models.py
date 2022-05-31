from django.db import models


STATUS = ((1, "Bookable"), (0, "Booking closed"))


class Level(models.Model):
    name = models.CharField(max_length=4)
    part = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.name} Part {self.part}'


class Format(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=254)
    level = models.ForeignKey(
        'Level', null=True, blank=False, on_delete=models.CASCADE
    )
    format = models.ForeignKey(
        'Format', null=True, blank=False, on_delete=models.CASCADE
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    startdate = models.DateField()
    weekday = models.CharField(max_length=254)
    starttime = models.TimeField()
    duration = models.CharField(max_length=254)
    status = models.IntegerField(choices=STATUS, default=1)
    limit = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name
