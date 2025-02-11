from .forms import PostwForm
# Register your models here.

from .models import Poste, Postw, People, News, Commentw, Comment, Commente
from django.contrib import admin
from app1.models import Post  # Импортируйте вашу модель

# Регистрация модели в админке
admin.site.register(Post)
admin.site.register(Poste)
admin.site.register(Postw)
admin.site.register(People)
admin.site.register(News)
admin.site.register(Commente)
admin.site.register(Comment)
admin.site.register(Commentw)
