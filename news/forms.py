from django import forms

from news.models.category_model import Categories
from news.models.news_model import News


class CreateCategoriesForm(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=200)

    class Meta:
        model = Categories
        fields = ["name"]


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]
