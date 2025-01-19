"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from app1 import views
# from django.contrib import admin
from django.urls import path
from app1.views import index_page, a_page, create, post_page, chat_page, e_page, createe, s_page, createw, access_view
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index_page, name='index_page'),
    path('a/', a_page),
    path('create/', views.create, name='create'),
    path('posts/', views.post_page, name='post_page'),
    path('chat/', chat_page, name='chat'),
    path('e/', e_page, name='e_page'),
    path('createe/', createe, name='createe'),
    path('s/', s_page, name='s_page'),
    path('creates/', createw, name='createw'),
    path('',access_view, name='access_key'),
    path('protected/', views.protected_page, name='protected_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.PAGE1_MEDIA_URL, document_root=settings.PAGE1_MEDIA_ROOT) + \
    static(settings.PAGE2_MEDIA_URL, document_root=settings.PAGE2_MEDIA_ROOT)

