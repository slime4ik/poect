from .forms import PostwForm
# Register your models here.

from .models import AccessKey, Poste, Postw
from django.contrib import admin
from app1.models import Post  # Импортируйте вашу модель

# Регистрация модели в админке
admin.site.register(Post)
admin.site.register(AccessKey)
admin.site.register(Poste)
admin.site.register(Postw)
