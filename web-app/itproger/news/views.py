from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView



def news_home(request):
    news = Articles.objects.order_by('-date') # Упорядочить по тайтлу. Если нужно в обратном порядке, то аргумент '-title'
    #news = Articles.objects.order_by('-date')[:2] Получим срез только две записи. [0] и [1]
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm #Показываем шо мы юзаем форму артиклс форм

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news-delete.html'

    success_url = '/news/'


def create(request):

    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') #После проверки формы на валидность. Метод redirect переадресовывает на home
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)