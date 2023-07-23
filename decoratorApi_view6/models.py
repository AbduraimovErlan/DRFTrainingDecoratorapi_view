from django.db import models

class Book6(models.Model):
    title = models.CharField(max_length=199)
    descriptions = models.TextField()


    def __str__(self):
        return self.title