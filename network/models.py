from django.db import models


class Contact(models.Model):
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    building_number = models.CharField(max_length=16)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.email} - {self.country}, {self.city}, {self.street}, {self.building_number}'
