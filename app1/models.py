from django.db import models
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=100)
    text  = models.TextField(blank=False)
    image = models.ImageField(upload_to='images', blank=True, null=True)  # 'images/' — папка, куда будут загружаться изображения

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'АЭМ'

@receiver(post_delete, sender=Post)
def delete_image_on_post_delete(sender, instance, **kwargs):
    """Удаление файла изображения из папки хранения после удаления объекта из БД."""
    if instance.image:
        if os.path.isfile(instance.image.path):  # Проверка существования файла
            os.remove(instance.image.path)  # Удаление файла
    def __str__(self):
        return self.key

class Poste(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=100)
    text  = models.TextField(blank=False)
    image = models.ImageField(upload_to='imagese', blank=True, null=True)  # 'images/' — папка, куда будут загружаться изображения

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'ЭОВС'


@receiver(post_delete, sender=Post)
def delete_image_on_post_delete(sender, instance, **kwargs):
    """Удаление файла изображения из папки хранения после удаления объекта из БД."""
    if instance.image:
        if os.path.isfile(instance.image.path):  # Проверка существования файла
            os.remove(instance.image.path)  # Удаление файла


class Postw(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=100)
    text  = models.TextField(blank=False)
    image = models.ImageField(upload_to='imagess', blank=True, null=True)  # 'images/' — папка, куда будут загружаться изображения

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Темы'
        verbose_name_plural = 'СЭВС'


@receiver(post_delete, sender=Post)
def delete_image_on_post_delete(sender, instance, **kwargs):
    """Удаление файла изображения из папки хранения после удаления объекта из БД."""
    if instance.image:
        if os.path.isfile(instance.image.path):  # Проверка существования файла
            os.remove(instance.image.path)  # Удаление файла

class AccessKey(models.Model):
    key = models.CharField(max_length=50, unique=True)  # Уникальный код
    assigned_name = models.CharField(max_length=100, default=False)  # Имя, связанное с кодом
    used = models.BooleanField(default=False)  # Отметка, использован ли ключ

    def __str__(self):
        return f"{self.key} - {self.assigned_name} ({'Used' if self.used else 'Unused'})"