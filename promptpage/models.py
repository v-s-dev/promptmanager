# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

class Prompt(models.Model):
    name = models.CharField(max_length=100)
    prompt = models.TextField()
    notes = models.TextField(blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='prompts')

    def __str__(self):
        return self.name
