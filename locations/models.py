from django.db import models


class City(models.Model):
    city = models.CharField(max_length=5)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'Citites'


class Location(models.Model):
    address = models.CharField(max_length=256)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.city.city + self.address
