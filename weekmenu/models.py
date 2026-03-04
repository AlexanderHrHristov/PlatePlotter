from django.db import models


class WeekMenu(models.Model):
    start_date = models.DateField(
        unique=True,
        verbose_name="Начална дата на седмицата",
    )

    notes = models.TextField(
        blank=True,
        verbose_name="Бележки",
    )

    def __str__(self):
        return f"Седмица от {self.start_date}"


class Meal(models.Model):

    DAY_CHOICES = [
        (1, "Понеделник"),
        (2, "Вторник"),
        (3, "Сряда"),
        (4, "Четвъртък"),
        (5, "Петък"),
        (6, "Събота"),
        (7, "Неделя"),
    ]

    MEAL_TYPE_CHOICES = [
        ("breakfast", "Закуска"),
        ("lunch", "Обяд"),
        ("snack", "Междинно хранене"),
        ("dinner", "Вечеря"),
    ]

    week_menu = models.ForeignKey(
        WeekMenu,
        on_delete=models.CASCADE,
        related_name="meals",
    )

    day = models.IntegerField(
        choices=DAY_CHOICES,
        verbose_name="Ден",
    )

    meal_type = models.CharField(
        max_length=20,
        choices=MEAL_TYPE_CHOICES,
        verbose_name="Хранене",
    )

    dish = models.ForeignKey(
        "meals.Dish",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Ястие",
    )

    eating_out = models.BooleanField(
        default=False,
        verbose_name="Хранене навън",
    )

    notes = models.TextField(
        blank=True,
        verbose_name="Бележки",
    )

    class Meta:
        unique_together = ("week_menu", "day", "meal_type")

    def __str__(self):
        return f"{self.week_menu} - {self.get_day_display()} {self.get_meal_type_display()}"