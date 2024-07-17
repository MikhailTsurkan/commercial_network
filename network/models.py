from django.db import models


class Contact(models.Model):
    supplier = models.ForeignKey(
        to="Supplier",
        on_delete=models.CASCADE,
        related_name="contacts",
        verbose_name="Supplier",
        help_text="Supplier to which contact belongs"
    )

    email = models.EmailField(
        unique=True,
        verbose_name="Email address",
        help_text="Email address for contacting"
    )
    country = models.CharField(
        max_length=128,
        verbose_name="Country name",
        help_text="Country of company location"
    )
    city = models.CharField(
        max_length=128,
        verbose_name="City name",
        help_text="City of company location"
    )
    street = models.CharField(
        max_length=128,
        verbose_name="Street name",
        help_text="Street where company is located"
    )
    building_number = models.CharField(
        max_length=16,
        verbose_name="Building number",
        help_text="Building number in street where company is located"
    )

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        help_text = 'Список контактов компаний'

    def __str__(self):
        return f'{self.email} - {self.country}, {self.city}, {self.street}, {self.building_number}'
