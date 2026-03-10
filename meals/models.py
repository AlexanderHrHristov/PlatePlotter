from django.db import models
from django.core.validators import MinValueValidator
from inventory.models import Product


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

    def total_calories(self):
        total = 0

        for item in self.recipeitem_set.all():
            total += (item.quantity_needed / 100) * item.product.calories_per_100

        return round(total, 2)

    def total_protein(self):
        total = 0

        for item in self.recipeitem_set.all():
            total += (item.quantity_needed / 100) * item.product.protein_per_100

        return round(total, 2)

    def total_carbs(self):
        total = 0

        for item in self.recipeitem_set.all():
            total += (item.quantity_needed / 100) * item.product.carbs_per_100

        return round(total, 2)

    def total_fat(self):
        total = 0

        for item in self.recipeitem_set.all():
            total += (item.quantity_needed / 100) * item.product.fat_per_100

        return round(total, 2)


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