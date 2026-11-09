from django.db import models

# Create your models here.

class Course(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    duration = models.CharField(max_length=200)

    trainer = models.CharField(max_length=200)

    language = models.CharField(max_length=200)

    fee = models.DecimalField(max_digits=10,decimal_places=2)

    cover_picture = models.ImageField(upload_to="cover_pics",null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name