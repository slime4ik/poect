from .forms import PostwForm
# Register your models here.

from .models import Poste, Postw, People, News
from django.contrib import admin
from app1.models import Post  # Импортируйте вашу модель

# Регистрация модели в админке
admin.site.register(Post)
admin.site.register(Poste)
admin.site.register(Postw)
admin.site.register(People)
admin.site.register(News)

