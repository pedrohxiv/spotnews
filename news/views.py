from django.shortcuts import render, get_object_or_404

from news.models import News


def home(request):
    news = News.objects.all()
    return render(request, 'home.html', {'news': news})


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news_details.html', {'news': news})
