from enum import Enum, EnumMeta

from django.db import models

from aristotle import settings


class ViolationCategoryMeta(EnumMeta):
    def __iter__(self):
        return ((tag.name, tag.value) for tag in super().__iter__())


class ViolationCategory(Enum, metaclass=ViolationCategoryMeta):
    RED_LINE = "Red line parking"


class Ticket(models.Model):
    violation = models.CharField(max_length=10, choices=ViolationCategory)
    plate_number = models.CharField(max_length=10)
    location = models.CharField(max_length=256)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

