from django.db import models
import datetime

class order(models.Model):
    table = models.PositiveSmallIntegerField(max_length=1, default=0)
    data = models.DateField(default=datetime.date.today)
    name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')

class table(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    TABLE_FORM = (
        ('elips','ELIPS'),
        ('square', 'SQUARE'),
    )
    amount = models.PositiveSmallIntegerField(max_length=1, default=0)
    table_form = models.CharField(max_length=10, choices=TABLE_FORM, default='square')
    coordinates_x = models.PositiveSmallIntegerField(max_length=1, default=0)
    coordinates_y = models.PositiveSmallIntegerField(max_length=1, default=0)
    width = models.PositiveSmallIntegerField(max_length=1, default=100)
    height = models.PositiveSmallIntegerField(max_length=1, default=60)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title
