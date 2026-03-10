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

    def total_calories_for_day(self, day):
        total = 0

        meals = self.meals.filter(day=day)

        for meal in meals:
            total += meal.total_calories()

        return round(total, 2)

    def total_protein_for_day(self, day):
        total = 0

        meals = self.meals.filter(day=day)

        for meal in meals:
            total += meal.total_protein()

        return round(total, 2)

    def total_carbs_for_day(self, day):
        total = 0

        meals = self.meals.filter(day=day)

        for meal in meals:
            total += meal.total_carbs()

        return round(total, 2)

    def total_fat_for_day(self, day):
        total = 0

        meals = self.meals.filter(day=day)

        for meal in meals:
            total += meal.total_fat()

        return round(total, 2)

    def total_calories_for_week(self):
        total = 0

        for meal in self.meals.all():
            total += meal.total_calories()

        return round(total, 2)

    def total_protein_for_week(self):
        total = 0

        for meal in self.meals.all():
            total += meal.total_protein()

        return round(total, 2)

    def total_carbs_for_week(self):
        total = 0

        for meal in self.meals.all():
            total += meal.total_carbs()

        return round(total, 2)

    def total_fat_for_week(self):
        total = 0

        for meal in self.meals.all():
            total += meal.total_fat()

        return round(total, 2)


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

    def total_calories(self):
        if self.dish:
            return self.dish.total_calories()
        return 0

    def total_protein(self):
        if self.dish:
            return self.dish.total_protein()
        return 0

    def total_carbs(self):
        if self.dish:
            return self.dish.total_carbs()
        return 0

    def total_fat(self):
        if self.dish:
            return self.dish.total_fat()
        return 0