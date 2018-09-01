from enum import Enum, EnumMeta

from django.db import models

from aristotle import settings
from locations.models import Location


class ViolationCategoryMeta(EnumMeta):
    def __iter__(self):
        return ((tag.name, tag.value) for tag in super().__iter__())


class ViolationCategory(Enum, metaclass=ViolationCategoryMeta):
    RED_LINE = "Red line parking"


class Ticket(models.Model):
    violation = models.CharField(max_length=10, choices=ViolationCategory)
    plate_number = models.CharField(max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def get_city(self):
        return self.location.city

    def __str__(self):
        return self.plate_number + ' (' + self.violation + ')'
