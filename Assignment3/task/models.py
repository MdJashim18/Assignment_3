from django.db import models
from category.models import Category
# Create your models here.


class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_complate = models.BooleanField(default=False)
    date = models.DateField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title