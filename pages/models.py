from django.db import models

# Create your models here.
class destination(models.Model):
    
    name = models.CharField(max_length =100 ,default='SOME STRING')
    image = models.ImageField(upload_to='pics', default='SOME STRING')
    description = models.TextField(max_length=300, default='SOME STRING')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

