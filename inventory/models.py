from django.db import models
from django.core.validators import MinValueValidator


class Store(models.Model):
    name = models.CharField(
        max_length=40,
        unique=True,
        verbose_name="Магазин",  # магазинът, от който най-често купувам този продукт (Билла, Лидл, бакалия...)
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    UNIT_CHOICES = [
        ("g", "Грамове (g)"),
        ("pcs", "Опаковка (бр.)"),  # ползвам за продукти на брой/опаковка + течности (мляко, бира и т.н.)
    ]

    name = models.CharField(
        max_length=50,
        verbose_name="Продукт",
    )

    brand = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Марка",  # ако има различни производители: "Верея", "Добрев", "Pilos" и т.н.
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Магазин",
    )

    unit = models.CharField(
        max_length=10,
        choices=UNIT_CHOICES,
        verbose_name="Мерна единица",
    )

    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Цена",
        help_text="Цена за килограм или опаковка",  # за течности - цена за опаковка!
    )

    is_basic = models.BooleanField(
        default=False,
        verbose_name="Основен продукт",
        help_text="Продукт, от който винаги трябва да има наличност.",
    )

    class Meta:
        unique_together = ("name", "brand")  

    def full_name(self):
        return f"{self.name} {self.brand}".strip()

    def __str__(self):
        return self.full_name()


class Inventory(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="inventory",
        verbose_name="Продукт",
    )

    available_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Налично количество",
    )

    minimum_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Минимално количество",
    )

    def __str__(self):
        # g -> "g", pcs -> "бр."
        unit_label = "g" if self.product.unit == "g" else "бр."
        return f"{self.product} - {self.available_quantity} {unit_label}"