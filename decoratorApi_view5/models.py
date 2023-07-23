from django.db import models

class Book5(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField()


    def __str__(self):
        return self.title


