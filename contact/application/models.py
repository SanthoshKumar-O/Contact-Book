from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
class Number(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    number=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'number')
    def __str__(self):
        return self.name

class contactAdmin(admin.ModelAdmin):
    list_display=['name','number','email','address']