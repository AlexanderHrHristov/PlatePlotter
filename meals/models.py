from django.db import models
from inventory.models import Product
from django.core.validators import MinValueValidator



class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

   
    products = models.ManyToManyField(
        Product,
        through="RecipeItem",
        related_name="dishes",
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    quantity_needed = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )

    note = models.CharField(max_length=120, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("dish", "product"),
                name="uq_recipeitem_dish_product",
            )
        ]

    def __str__(self):
        return f"{self.dish} - {self.product} ({self.quantity_needed} {self.product.unit})"