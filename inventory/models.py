from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    UNIT_CHOICES = [
        ('g', 'Грамове(g)'),
        ('ml', 'Милилитри (ml)'),
        ('pcs', 'Броя'),
    ]

    name = models.CharField(
        max_length= 50, 
        verbose_name="Продукт",
        unique= True,
        )
    
    unit = models.CharField(
        max_length=10,
        choices=UNIT_CHOICES,
        verbose_name='Количество',
    )

    energy_per_100 = models.PositiveIntegerField(
        max_length=10, 
        verbose_name='Килокалории',
    )
    
    protein_per_100 = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default='g',
        validators=[MinValueValidator(0)],
        verbose_name='Белтъчини',
    )
    
    carbs_per_100 = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default='g',
        validators=[MinValueValidator(0)],
        verbose_name='Въглехидрати',
    )

    fats_per_100 = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default='g',
        validators=[MinValueValidator(0)],
        verbose_name='Мазнини',
    )

    is_basic = models.BooleanField(
        default=False,
        verbose_name='Основен продукт',
        help_text='Основни продукти от които винаги трябва да има наличност'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Inventory(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='Налични продукти',
    )

    available_quantity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
    )

    minimun_quantity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)],
    )
        
    updated_at = models.DateTimeField(auto_now=True)

