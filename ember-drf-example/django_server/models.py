from django.db import models

class Summary(models.Model):
    id = models.CharField(max_length=50, unique=True, primary_key=True)
    total_runs = models.IntegerField(blank=True, null=True)
    total_tests = models.IntegerField(blank=True, null=True)
    average_yield = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)