from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import Post, Poste, Postw, People, News, Commentw, Commente, Comment
from .forms import PosteForm, PostForm, PostwForm, PeopleForm, CommentForm, CommenteForm, CommentwForm
from .forms import AccessKeyForm
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import user_logged_in, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

@login_required
def index_page(request):
    news_list = News.objects.order_by('-id')  # или ваш запрос для получения списка новостей
    return render(request, 'home.html', {'news_list': news_list})

@login_required
def a_page(request):
    posts = Post.objects.order_by('-id')  # Получаем QuerySet с записями
    paginator = Paginator(posts, 7)  # Передаем QuerySet в Paginator
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'a.html', {'title': '', 'Posts': posts})

#СОЗДАНИЕ ПОСТА В АЭМ
@login_required
def create(request):
    error = ''
    image_url = None
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Обработка данных формы и файлов
        if form.is_valid():
            image_url = 'images/load.gif'
            messages.success(request, 'Пост добавляется давай жди емае')
            # Создаем объект поста без сохранения в БД
            post = form.save(commit=False)
            post.user = request.user  # Присваиваем текущего пользователя
            post.save()  # Сохраняем пост в БД
            return redirect('/a/')  # Перенаправляем после сохранения
        else:
            error = 'Ты бл заполни нормально ее дебил'
    else:
        form = PostForm()  # Пустая форма для первого загрузки страницы

    # Получение всех записей из базы данных
    posts = Post.objects.all()

    context = {
        'form': form,
        'error': error,
        'posts': posts,  # Добавляем посты в контекст для отображения
        'image_url' : image_url
    }
    return render(request, 'create.html', context)






'''def posts_view(request):
    posts = Post.objects.select_related('user').all()
    return render(request, 'posts.html', {'Posts': posts})'''

@login_required
# app1/views.py
def e_page(request):
    postes = Poste.objects.order_by('-id')
    paginator = Paginator(postes, 7)  # Передаем QuerySet в Paginator
    page_number = request.GET.get('page', 1)
    try:
        postes = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        postes = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        postes = paginator.page(paginator.num_pages)
    return render(request, 'e.html', {'title': '', 'Postes' : postes })

@login_required
def createe(request):
    error=''
    image_url = None
    if request.method == 'POST':
        form = PosteForm(request.POST, request.FILES)  # Обработка данных формы и файлов
        if form.is_valid():
            image_url = 'images/load.gif'
            messages.success(request, 'Пост добавляется давай жди емае')
            post = form.save(commit=False)
            post.user = request.user  # Присваиваем текущего пользователя
            post.save()  # Сохраняем пост в БД
            return redirect('/e/')
    else:
        error = 'ты бл заполни нормально ее дебил'

    # Получение всех записей из базы данных
    Postes = Poste.objects.all()
    form = PosteForm()

    context ={
        'form': form,
        'error': error,
        'image_url' : image_url
    }
    return render(request, 'createe.html', context)

@login_required
def s_page(request):
    postws = Postw.objects.order_by('-id')
    paginator = Paginator(postws, 7)  # Передаем QuerySet в Paginator
    page_number = request.GET.get('page', 1)
    try:
        postws = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        postws = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        postws = paginator.page(paginator.num_pages)
    return render(request, 's.html', {'title': '', 'Postws' : postws })
@login_required
def createw(request):
    error=''
    image_url = None
    if request.method == 'POST':
        form = PostwForm(request.POST, request.FILES)  # Обработка данных формы и файлов
        if form.is_valid():
            image_url = 'images/load.gif'
            messages.success(request, 'Пост добавляется давай жди емае')
            post = form.save(commit=False)
            post.user = request.user  # Присваиваем текущего пользователя
            post.save()  # Сохраняем пост в БД
            return redirect('/s/')
    else:
        error = 'ты бл заполни нормально ее дебил'

    # Получение всех записей из базы данных

    Postws = Postw.objects.all()
    form = PostwForm()

    context ={
        'form': form,
        'error': error,
        'image_url' : image_url
    }
    return render(request, 'creates.html', context)

def signin(request):
    # Если пользователь уже авторизован, перенаправляем на /home/
    if request.user.is_authenticated:
        return redirect("index_page")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Авторизация пользователя
            login(request, user)
            # Перенаправление на главную страницу
            return redirect("index_page")
        else:
            # Если аутентификация не удалась
            messages.error(request, 'Чото ты не правильно ввел -_-')
            return redirect('signin')

    # Если метод не POST, отображаем форму входа
    return render(request, 'loging/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Вышли успешно)")
    return redirect('signin')

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Comment.objects.create(post=post, user=request.user, text=text)
    
    return redirect(request.META.get("HTTP_REFERER", "/"))

@login_required
def add_commente(request, post_id):
    post = get_object_or_404(Poste, id=post_id)
    
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Commente.objects.create(post=post, user=request.user, text=text)
    return redirect(request.META.get("HTTP_REFERER", "/"))

@login_required
def add_commentw(request, post_id):
    post = get_object_or_404(Postw, id=post_id)
    
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Commentw.objects.create(post=post, user=request.user, text=text)
    
    return redirect(request.META.get("HTTP_REFERER", "/"))
#ДЛЯ АЭМ 
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Проверяем, что текущий пользователь — автор поста
    if post.user != request.user:
        return redirect('/a/')  # Если это не автор, перенаправляем на главную

    if request.method == 'POST':
        post.name = request.POST['name']  # Обновляем название
        post.text = request.POST['text']  # Обновляем текст

        # Обрабатываем изображение, если оно было загружено
        if 'image' in request.FILES:
            post.image = request.FILES['image']

        post.save()
        return redirect('/a/')  # Перенаправление на главную страницу

    return render(request, 'a.html', {'Posts': Post.objects.all()})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Проверяем, что текущий пользователь — автор поста
    if post.user != request.user:
        return redirect('/a/')  # Если это не автор, перенаправляем на главную

    post.delete()
    return redirect('/a/')  # Или перенаправить на страницу с постами

#ДЛЯ ЭОВС
def edite_post(request, post_id):
    post = get_object_or_404(Poste, id=post_id)

    # Проверяем, что текущий пользователь — автор поста
    if post.user != request.user:
        return redirect('/e/')  # Если это не автор, перенаправляем на главную

    if request.method == 'POST':
        post.name = request.POST['name']  # Обновляем название
        post.text = request.POST['text']  # Обновляем текст

        # Обрабатываем изображение, если оно было загружено
        if 'image' in request.FILES:
            post.image = request.FILES['image']

        post.save()
        return redirect('/e/')  # Перенаправление на главную страницу

    return render(request, 'e.html', {'Postes': Post.objects.all()})

#ДЛЯ СЭВС
def editw_post(request, post_id):
    post = get_object_or_404(Postw, id=post_id)

    # Проверяем, что текущий пользователь — автор поста
    if post.user != request.user:
        return redirect('/s/')  # Если это не автор, перенаправляем на главную

    if request.method == 'POST':
        post.name = request.POST['name']  # Обновляем название
        post.text = request.POST['text']  # Обновляем текст

        # Обрабатываем изображение, если оно было загружено
        if 'image' in request.FILES:
            post.image = request.FILES['image']

        post.save()
        return redirect('/s/')  # Перенаправление на главную страницу

    return render(request, 's.html', {'Postws': Post.objects.all()})

def delete_poste(request, post_id):
    post = get_object_or_404(Poste, id=post_id)

    # Проверяем, что текущий пользователь — автор поста
    if post.user != request.user:
        return redirect('/e/')  # Если это не автор, перенаправляем на главную

    post.delete()
    return redirect('/e/')  # Или перенаправить на страницу с постами

def delete_postw(request, post_id):
    post = get_object_or_404(Postw, id=post_id)

    # Проверяем, что текущий пользователь — автор поста
    if post.user != request.user:
        return redirect('/s/')  # Если это не автор, перенаправляем на главную

    post.delete()
    return redirect('/s/')  # Или перенаправить на страницу с постами

