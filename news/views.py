from django.shortcuts import redirect, render, get_object_or_404

from news.forms import CreateCategoriesForm, CreateNewsForm
from news.models import Categories, News, Users


def home(request):
    news = News.objects.all()
    return render(request, 'home.html', {'news': news})


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news_details.html', {'news': news})


def create_categories(request):
    form = CreateCategoriesForm()

    if request.method == "POST":
        form = CreateCategoriesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home-page")

    return render(request, 'categories_form.html', {'form': form})


def create_news(request):
    form = CreateNewsForm()

    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("home-page")

    authors = Users.objects.all()
    categories = Categories.objects.all()

    return render(
        request,
        'news_form.html',
        {'form': form, 'authors': authors, 'categories': categories}
    )
