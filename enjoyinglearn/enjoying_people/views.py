from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView


from .models import *
from .forms import *

menu = [{"title": "О сайте", "url_name": 'about'},
        {"title": "Добавить статью", "url_name": 'add_page'},
        {"title": "Обратная связь", "url_name": 'contact'},
        {"title": "Войти", "url_name": 'login'},
]


class PeopleHome(ListView):
    model = People
    template_name = 'enjoying_people/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['menu'] = {'title': 'Главная страница'}
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return People.objects.filter(is_publiched=True)


def about(request):
    return render(request, 'enjoying_people/about.html', {'menu': menu, 'title': 'О сайте'})


def add_page(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'enjoying_people/addpage.html', {"form": form, "menu": menu, 'title': "Добавить пост"})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(People, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'enjoying_people/post.html', context=context)


def show_category(request, cat_id):
    posts = People.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'enjoying_people/index.html', context=context)



