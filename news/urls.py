from django.urls import path

from news.views import home, news_details, create_categories, create_news


urlpatterns = [
    path("", home, name='home-page'),
    path("news/<int:id>/", news_details, name="news-details-page"),
    path("categories", create_categories, name="categories-form"),
    path("news/", create_news, name="news-form"),
]
