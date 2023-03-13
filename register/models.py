from django.db import models


class Register(models.Model):

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

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    car = models.CharField(choices=CAR_CHOICES, max_length=60)
    phonenum = models.IntegerField()



