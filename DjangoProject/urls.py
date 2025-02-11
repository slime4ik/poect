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

from django.urls import re_path
from django.views.static import serve
from app1 import views
# from django.contrib import admin
from django.urls import path
from app1.views import index_page, a_page, create, e_page, createe, s_page, createw, signin, add_comment, add_commente, add_commentw
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', index_page, name='index_page'),
    path('a/', a_page),
    path('create/', views.create, name='create'),
#    path('posts/', views.post_page, name='post_page'),
    path('e/', e_page, name='e_page'),
    path('createe/', createe, name='createe'),
    path('s/', s_page, name='s_page'),
    path('creates/', createw, name='createw'),
    path('', signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
    path('add_commente/<int:post_id>/', add_commente, name='add_commente'),
    path('add_commentw/<int:post_id>/', add_commentw, name='add_commentw'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('deletee/<int:post_id>/', views.delete_poste, name='delete_poste'),
    path('deletew/<int:post_id>/', views.delete_postw, name='delete_postw'),
    path('edite/<int:post_id>/', views.edite_post, name='edite_post'),
    path('editw/<int:post_id>/', views.editw_post, name='editw_post'),
    re_path(r'^a/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^e/(?P<path>.*)$', serve, {'document_root': settings.PAGE1_MEDIA_ROOT}),
    re_path(r'^s/(?P<path>.*)$', serve, {'document_root': settings.PAGE2_MEDIA_ROOT}),
    re_path(r'^home/(?P<path>.*)$', serve, {'document_root': settings.PAGE3_MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
    static(settings.PAGE1_MEDIA_URL, document_root=settings.PAGE1_MEDIA_ROOT) + \
    static(settings.PAGE2_MEDIA_URL, document_root=settings.PAGE2_MEDIA_ROOT) + \
    static(settings.PAGE3_MEDIA_URL, document_root=settings.PAGE3_MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.PAGE1_MEDIA_URL, document_root=settings.PAGE1_MEDIA_ROOT)
    urlpatterns += static(settings.PAGE2_MEDIA_URL, document_root=settings.PAGE2_MEDIA_ROOT)
    urlpatterns += static(settings.PAGE3_MEDIA_URL, document_root=settings.PAGE3_MEDIA_ROOT)

