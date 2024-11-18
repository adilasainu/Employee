from django.db import models

# Create your models here.
class Emp1(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    profile=models.ImageField(upload_to="images")
    pdf=models.FileField(upload_to="pdf")

    def __str__(self):
        return self.name
