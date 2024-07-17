from django.db import models


class Contact(models.Model):
    """
    Модель контакта, содержащая контактные данные
    """
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
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        help_text = 'Contact details'

    def __str__(self):
        return f'{self.email} - {self.country}, {self.city}, {self.street}, {self.building_number}'


class Product(models.Model):
    """
    Модель продукта, описывающая продукт, его модель и дату выхода на рынок
    """
    supplier = models.ManyToManyField(
        to="Supplier",
        related_name="products",
        verbose_name="Supplier",
        help_text="Supplier of product"
    ),

    name = models.CharField(
        max_length=128,
        verbose_name="Product name",
        help_text="Name of the product"
    ),
    model = models.CharField(
        max_length=128,
        verbose_name="Product model",
        help_text="Model of the product"
    ),
    release_date = models.DateField(
        verbose_name="Release date",
        help_text="Date when product was released on market"
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        help_text = 'Product details'

    def __str__(self):
        return f'{self.name} - {self.model}'

