from django.db import models
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=100)
    text  = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)  # 'images/' — папка, куда будут загружаться изображения
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


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
    name = models.CharField(blank=True, max_length=100)
    text  = models.TextField(blank=True)
    image = models.ImageField(upload_to='imagess', blank=True, null=True)  # 'images/' — папка, куда будут загружаться изображения
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


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

class People(models.Model):
    # Уникальный пароль (ключ)
    password = models.CharField(blank=False, max_length=4, unique=True)
    # Имя пользователя
    name = models.CharField(blank=False, max_length=50, unique=True)
    # Флаг, указывающий, был ли ключ уже использован
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.password}"

class News(models.Model):
    name = models.CharField(blank=True, max_length=100)
    text  = models.TextField(blank=True)
    image = models.ImageField(upload_to='news', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

@receiver(post_delete, sender=News)
def delete_image(sender, instance, **kwargs):
    # Проверяем, если у объекта есть изображение
    if instance.image:
        # Формируем путь к изображению
        image_path = instance.image.path
        # Проверяем, существует ли файл на диске, и удаляем его
        if os.path.isfile(image_path):
            os.remove(image_path)

#КОМЕНТЫ ДЛЯ Post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # Комментарий привязан к посту
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, оставивший комментарий
    text = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}"
    
#КОМЕНТЫ ДЛЯ Poste
class Commente(models.Model):
    post = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name="commentse")  # Комментарий привязан к посту
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, оставивший комментарий
    text = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}"
    
#КОМЕНТЫ ДЛЯ Postw
class Commentw(models.Model):
    post = models.ForeignKey(Postw, on_delete=models.CASCADE, related_name="commentsw")  # Комментарий привязан к посту
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Пользователь, оставивший комментарий
    text = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}"