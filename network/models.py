from django.db import models


class Contact(models.Model):
    """
    Contact model for contacting with suppliers.
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
    Model describing a product
    """
    suppliers = models.ManyToManyField(
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


SUPPLIER_TYPES = [
    ('factory', 'Factory'),
    ('retailer', 'Retailer'),
    ('individual', 'Individual'),
]


class Supplier(models.Model):
    """
    Model describing a supplier
    """
    supplier = models.ForeignKey(
        to="self",
        on_delete=models.PROTECT,
        related_name="buyers",
        verbose_name="Supplier",
        help_text="Supplier of current supplier",
        null=True,
        blank=True
    ),

    name = models.CharField(
        max_length=128,
        verbose_name="Supplier name",
        help_text="Name of the supplier"
    ),
    debt = models.DecimalField(
        verbose_name="Debt",
        decimal_places=2,
        max_digits=10,
        default=0,
        help_text="Supplier's current debt""'"
    ),
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
        help_text="Date when supplier was created"
    )

    supplier_type = models.CharField(
        choices=SUPPLIER_TYPES,
        verbose_name="Supplier type",
        help_text="Type of supplier"
    )

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        help_text = 'Supplier details'

    def __str__(self):
        return f'{self.name}'
