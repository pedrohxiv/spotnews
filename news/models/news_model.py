from django.db import models

from news.validators import validate_title


class News(models.Model):
    title = models.CharField(max_length=200, validators=[validate_title])
    content = models.TextField()
    author = models.ForeignKey(
        "Users",
        on_delete=models.CASCADE,
        related_name="news")
    created_at = models.DateField()
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    categories = models.ManyToManyField("Categories")

    def __str__(self):
        return self.title
