from django.db import models
from django.utils.translation import gettext_lazy


class Contact(models.Model):
    """
    Contact model for contacting with suppliers.
    """
    supplier = models.ForeignKey(
        to="Supplier",
        on_delete=models.CASCADE,
        related_name="contacts",
        verbose_name=gettext_lazy("Supplier"),
        help_text=gettext_lazy("Supplier to which contact belongs")
    )

    email = models.EmailField(
        unique=True,
        verbose_name=gettext_lazy("Email address"),
        help_text=gettext_lazy("Email address for contacting")
    )
    country = models.CharField(
        max_length=128,
        verbose_name=gettext_lazy("Country name"),
        help_text=gettext_lazy("Country of company location")
    )
    city = models.CharField(
        max_length=128,
        verbose_name=gettext_lazy("City name"),
        help_text=gettext_lazy("City of company location")
    )
    street = models.CharField(
        max_length=128,
        verbose_name=gettext_lazy("Street name"),
        help_text=gettext_lazy("Street where company is located")
    )
    building_number = models.CharField(
        max_length=16,
        verbose_name=gettext_lazy("Building number"),
        help_text=gettext_lazy("Building number in street where company is located")
    )

    class Meta:
        verbose_name = gettext_lazy('Contact')
        verbose_name_plural = gettext_lazy('Contacts')
        help_text = gettext_lazy('Contact details')

    def __str__(self):
        return f'{self.email} - {self.country}, {self.city}, {self.street}, {self.building_number}'


class Product(models.Model):
    """
    Model describing a product
    """
    suppliers = models.ManyToManyField(
        to="Supplier",
        related_name="products",
        verbose_name=gettext_lazy("Supplier"),
        help_text=gettext_lazy("Supplier of product")
    ),

    name = models.CharField(
        max_length=128,
        verbose_name=gettext_lazy("Product name"),
        help_text=gettext_lazy("Name of the product")
    ),
    model = models.CharField(
        max_length=128,
        verbose_name=gettext_lazy("Product model"),
        help_text=gettext_lazy("Model of the product")
    ),
    release_date = models.DateField(
        verbose_name=gettext_lazy("Release date"),
        help_text=gettext_lazy("Date when product was released on market")
    )

    class Meta:
        verbose_name = gettext_lazy('Product')
        verbose_name_plural = gettext_lazy('Products')
        help_text = gettext_lazy('Product details')

    def __str__(self):
        return f'{self.name} - {self.model}'


SUPPLIER_TYPES = [
    ('factory', gettext_lazy('Factory')),
    ('retailer', gettext_lazy('Retailer')),
    ('individual', gettext_lazy('Individual')),
]


class Supplier(models.Model):
    """
    Model describing a supplier
    """
    supplier = models.ForeignKey(
        to="self",
        on_delete=models.PROTECT,
        related_name="buyers",
        verbose_name=gettext_lazy("Supplier"),
        help_text=gettext_lazy("Supplier of current supplier"),
        null=True,
        blank=True
    ),

    name = models.CharField(
        max_length=128,
        verbose_name=gettext_lazy("Supplier name"),
        help_text=gettext_lazy("Name of the supplier")
    ),
    debt = models.DecimalField(
        verbose_name=gettext_lazy("Debt"),
        decimal_places=2,
        max_digits=10,
        default=0,
        help_text=gettext_lazy("Supplier's current debt")
    ),
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=gettext_lazy("Created at"),
        help_text=gettext_lazy("Date when supplier was created")
    )

    supplier_type = models.CharField(
        choices=SUPPLIER_TYPES,
        verbose_name=gettext_lazy("Supplier type"),
        help_text=gettext_lazy("Type of supplier")
    )

    class Meta:
        verbose_name = gettext_lazy('Supplier')
        verbose_name_plural = gettext_lazy('Suppliers')
        help_text = gettext_lazy('Supplier details')

    def __str__(self):
        return f'{self.name}'
