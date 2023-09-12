from django.db import models


class registertb(models.Model):
    email=models.CharField(max_length=500)
    passw=models.CharField(max_length=300)

class adproduct(models.Model):
    modelname=models.CharField(max_length=500)
    modelcolor=models.CharField(max_length=500)
    price=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to='product/')
    productsize=models.CharField(max_length=500)
    category=models.CharField(max_length=500)