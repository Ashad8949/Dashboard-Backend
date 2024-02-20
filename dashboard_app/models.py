# dashboard_app/models.py
from django.db import models

class Insight(models.Model):
    end_year = models.CharField(max_length=50, null=True)
    intensity = models.IntegerField(null=True)
    sector = models.CharField(max_length=100, null=True)
    topic = models.CharField(max_length=100, null=True)
    insight = models.TextField(blank=True)
    url = models.URLField(max_length=2000, null=True)
    region = models.CharField(max_length=100, null=True)
    start_year = models.CharField(max_length=50, blank=True, null=True)
    impact = models.CharField(max_length=100, null=True)
    added = models.DateTimeField()
    published = models.DateTimeField(null=True)
    country = models.CharField(max_length=100, null=True)
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=1000, null=True)
    title = models.CharField(max_length=1000, null=True)
    likelihood = models.IntegerField(null=True)
