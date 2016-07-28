from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    category = models.ForeignKey(Category)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Summary(models.Model):
    id = models.CharField(max_length=50, unique=True, primary_key=True)
    total_runs = models.IntegerField(blank=True, null=True)
    total_tests = models.IntegerField(blank=True, null=True)
    average_yield = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)