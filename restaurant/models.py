from django.db import models
from django.utils import timezone

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title}: {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name}: {self.booking_date}'