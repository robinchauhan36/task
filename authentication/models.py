from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(default='')
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    registration_choices = (
        (1, 'Vendor'),
        (2, 'Bidder'),
    )
    category = models.CharField(max_length=1, choices=registration_choices)

    def __str__(self):
        """
        get name
        """
        return self.first_name
