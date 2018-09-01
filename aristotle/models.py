from enum import Enum, EnumMeta

from django.db import models

from aristotle import settings


class ViolationCategoryMeta(EnumMeta):
    def __iter__(self):
        return ((tag, tag.value) for tag in super().__iter__())


class ViolationCategory(Enum, metaclass=ViolationCategoryMeta):
    RED_LINE = "Red line parking"


class Ticket(models.Model):
    violation = models.CharField(max_length=10, choices=ViolationCategory)
    plate_number = models.CharField(max_length=10)
    location = models.CharField(max_length=256)

