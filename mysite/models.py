from django.db import models

# Create your models here.


class drive(models.Model):
    title = models.CharField(max_length=180)
    file = models.FileField(upload_to="drive/%Y/%m/%d/")
    def __str__(self):
        return self.title