from django.db import models

class Draft(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/draft/{self.pk}'


    objects = models.Manager



