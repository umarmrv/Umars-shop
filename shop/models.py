from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Forien=получает кей с другого класс Category CASCADE удаляет вес курс если удалить одну котегорую с базы данных
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title} students {self.students_qty}"
