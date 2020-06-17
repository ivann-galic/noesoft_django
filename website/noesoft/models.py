from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100, default="No Name")
    last_mane = models.CharField(max_length=100, default="No last name")
    mail = models.CharField(max_length=100, default="No mail")
    phone = models.CharField(max_length=100, default="No phone")
    file = models.FileField(upload_to='cv/')
    message = models.TextField()
    job = models.CharField(max_length=100, default="No job")

    def __str__(self):
        return self.name + " " + self.last_mane