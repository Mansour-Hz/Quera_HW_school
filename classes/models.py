from django.db import models


class Classroom(models.Model):
    capacity = models.IntegerField()
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50, default='main')
    area = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'classes'
