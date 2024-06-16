from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)  # Текстовое поле
    created = models.DateField(default=timezone.now)  # Дата создания
    due_date = models.DateField()  # До какой даты нужно было сделать дело
    image = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name="Фотографія")
    category = models.BooleanField(default=False)  # Поле с правильным ключом default
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ["-created"]  # Сортировка дел по времени их создания

    def __str__(self):
        return self.title
