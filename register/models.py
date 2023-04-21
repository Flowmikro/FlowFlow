from django.db import models

CAR_CHOICES = [
        ('Porsche 911 Carrera', 'Porsche 911 Carrera'),
        ('Porsche 911 Turbo', 'Porsche 911 Turbo'),
        ('Porsche Cayman', 'Porsche Cayman'),
        ('Porsche Cayman GTS 4.0 ', 'Porsche Cayman GTS 4.0 '),
        ('Porsche Macan', 'Porsche Macan'),
        ('Porsche Panamera', 'Porsche Panamera'),
        ('Porsche Cayenne', 'Porsche Cayenne'),
        ('Porsche Taycan', 'Porsche Taycan'),
        ('Porsche Cayman', 'Porsche Cayman'),

    ]


class Service(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phonenum = models.IntegerField(max_length=11)
    car = models.CharField(choices=CAR_CHOICES, max_length=60)
    comm = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class CarBuy(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=150)
    phonenum = models.IntegerField(max_length=11)
    car = models.CharField(choices=CAR_CHOICES, max_length=60)

    def __str__(self):
        return self.name






