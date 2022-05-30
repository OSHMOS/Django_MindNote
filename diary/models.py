from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    feeling = models.CharField(max_length=80)
    score = models.IntegerField()
    dt_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title