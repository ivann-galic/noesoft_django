from django.db import models

class job(models.Model):
    name = models.CharField(max_length=255, default="No Name")
    infos = models.TextField()

    def __str__(self):
        return self.name