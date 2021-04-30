from django.db import models

# Create your models here.

class Item(models.Model):
    itemtype = models.CharField(max_length=200)
    itemcategory = models.CharField(max_length=200)
    name= models.CharField(max_length=200,unique=True)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.FloatField()
    quant=models.IntegerField()
    scale=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    offer=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
    Desc=models.TextField()
    #phone_number = forms.CharField(label='Phone Number', max_length=12, min_length=10)
    Img=models.ImageField(upload_to='fimages/')
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name