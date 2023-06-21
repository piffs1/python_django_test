from django.shortcuts import render
from .models import Articles
# Create your views here.

def news_home(request):
    news = Articles.objects.order_by('-date') # Упорядочить по тайтлу. Если нужно в обратном порядке, то аргумент '-title'
    #news = Articles.objects.order_by('-date')[:2] Получим срез только две записи. [0] и [1]
    return render(request, 'news/news_home.html', {'news': news})
