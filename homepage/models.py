from django.db import models

class Cow(models.Model):
    text = models.TextField(max_length=100)

    def __str__(self):
        return self.text