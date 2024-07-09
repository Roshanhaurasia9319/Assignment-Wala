from django.db import models

class User_data(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    WorkType = models.CharField(max_length=50)
    Sheet = models.IntegerField(null=False, blank=False)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    File = models.FileField(upload_to='pdfs/')
    def __str__(self):
        return self.Email
    
    
class App_content(models.Model):
    title = models.CharField(max_length=100, default="Comming Soon")
    image = models.ImageField(upload_to='images/', default="None")
    def __str__(self):
        return self.title