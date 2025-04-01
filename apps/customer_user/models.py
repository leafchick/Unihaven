from django.db import models

class CustomerUser(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email}'

class Reservations(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name='Reservations')
    accommodation = models.ForeignKey('Accommodation', on_delete=models.CASCADE, related_name='Accommodation')

    room_id = models.IntegerField()
    # Reserve-Period
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    rate_number = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} {self.check_in_date} {self.check_out_date} {self.rate_number}"


class Accommodation (models.Model):
    type = models.CharField(max_length=200)
    period_of_availability = models.CharField(max_length=200)
    number_of_beds = models.IntegerField()
    number_of_bedrooms = models.IntegerField()
    room_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Distance from HKU
    distance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.type} {self.period_of_availability}'
class Admin(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
