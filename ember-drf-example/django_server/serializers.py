from rest_framework import serializers

from django_server import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
