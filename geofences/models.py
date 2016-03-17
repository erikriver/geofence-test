from django.contrib.gis.db import models


class EmployeeArea(models.Model):
    name = models.CharField(max_length=100)
    area = models.MultiPolygonField()

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __str__(self):
        return self.name
