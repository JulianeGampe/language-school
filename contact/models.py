from django.db import models


REASON = (
    ("Level", "My Language Level"),
    ("Booking", "Existing Booking"),
    ("Help", "Help with Website"),
    ("Private", "Request private lesson"),
    ("Other", "Other Inquiry")
)


class Contact(models.Model):
    """
    Model for the contact form
    """
    name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phonenumber = models.CharField(max_length=20, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    reason = models.CharField(
        choices=REASON, default="Level",
        max_length=254,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name
