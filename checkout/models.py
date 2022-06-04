import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from courses.models import Course


class Order(models.Model):
    ordernumber = models.CharField(max_length=32, null=False, editable=False)
    fullname = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phonenumber = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    streetaddress1 = models.CharField(max_length=80, null=False, blank=False)
    streetaddress2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )

    def _generate_ordernumber(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added
        """
        self.total = self.lineitems.aggregate(
            Sum('lineitemtotal')
        )['lineitemtotal__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.ordernumber:
            self.ordernumber = self._generate_ordernumber()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ordernumber


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    course = models.ForeignKey(
        Course, null=False, blank=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitemtotal = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitemtotal = self.course.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Name: {self.course.name} on order {self.order.order_number}'
