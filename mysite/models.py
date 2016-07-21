from django.db import models

# Create your models here.


class drive(models.Model):
    file = models.FileField(upload_to="drive")
    def __str__(self):
        return self.file.name