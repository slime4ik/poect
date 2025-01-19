from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from .models import Post, Poste, Postw, AccessKey
from .forms import PosteForm, PostForm, PostwForm, AccessKeyForm
from .forms import AccessKeyForm
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index_page(request):
    return render(request, 'home.html')

@login_required
def a_page(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'a.html', {'title': '', 'Posts' : posts })

#СОЗДАНИЕ ПОСТА В АЭМ
@login_required
def create(request):
    error=''
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Обработка данных формы и файлов
        if form.is_valid():
            form.save()  # Сохраняем данные в БД
            return redirect('/a')
    else:
        error = 'ты бл заполни нормально ее дебил'

    # Получение всех записей из базы данных
    posts = Post.objects.all()
    form = PostForm()

    context ={
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)

@login_required
def post_page(request):
    # Обработка формы
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Обработка данных формы и файлов
        if form.is_valid():
            form.save()  # Сохраняем данные в БД

    else:
        form = PostForm()  # Пустая форма для GET-запроса

    # Получение всех записей из базы данных
    posts = Post.objects.all()

    # Передача формы и списка записей в шаблон
    return render(request, 'post_page.html', {'form': form, 'posts': posts})

@login_required
def chat_page(request):
    return render(request, 'chat.html')

@login_required
def posts_view(request):
    posts = Post.objects.select_related('user').all()
    return render(request, 'posts.html', {'Posts': posts})


# app1/views.py

from django.shortcuts import render, redirect
from .forms import AccessKeyForm
from .models import AccessKey
from django.http import HttpResponseForbidden




@login_required
def e_page(request):
    postes = Poste.objects.all()
    return render(request, 'e.html', {'title': '', 'Postes' : postes })

@login_required
def createe(request):
    error=''
    if request.method == 'POST':
        form = PosteForm(request.POST, request.FILES)  # Обработка данных формы и файлов
        if form.is_valid():
            form.save()  # Сохраняем данные в БД
            return redirect('/e')
    else:
        error = 'ты бл заполни нормально ее дебил'

    # Получение всех записей из базы данных
    Postes = Poste.objects.all()
    form = PosteForm()

    context ={
        'form': form,
        'error': error
    }
    return render(request, 'createe.html', context)

@login_required
def s_page(request):
    postws = Postw.objects.all()
    return render(request, 's.html', {'title': '', 'Postws' : postws })
@login_required
def createw(request):
    error=''
    if request.method == 'POST':
        form = PostwForm(request.POST, request.FILES)  # Обработка данных формы и файлов
        if form.is_valid():
            form.save()  # Сохраняем данные в БД
            return redirect('/s')
    else:
        error = 'ты бл заполни нормально ее дебил'

    # Получение всех записей из базы данных
    Postws = Postw.objects.all()
    form = PostwForm()

    context ={
        'form': form,
        'error': error
    }
    return render(request, 'creates.html', context)


from django.http import JsonResponse
from django.shortcuts import render

def access_view(request):
    if request.method == "POST":
        form = AccessKeyForm(request.POST)
        if form.is_valid():
            access_key = form.cleaned_data['access_key']
            try:
                key_entry = AccessKey.objects.get(key=access_key, used=False)
                key_entry.used = True
                key_entry.save()
                request.session['user_name'] = key_entry.assigned_name
                return JsonResponse({
                    'success': True,
                    'redirect_url': 'protected',  # URL куда перекидывать
                })
            except AccessKey.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'error_message': 'Invalid or already used key'
                })
    else:
        form = AccessKeyForm()

    return render(request, 'access_form.html', {'form': form})


def protected_page(request):
    # Проверка наличия имени в сессии
    user_name = request.session.get('user_name')

    if not user_name:
        return HttpResponseForbidden("Access denied")

    return render(request, 'protected_page.html', {'user_name': user_name})

