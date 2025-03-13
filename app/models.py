from django.db import models

# Create your models here.

# Create your models here.

class Item(models.Model):
    wallet = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.date} DT{self.date.strftime('%d/%m/%Y %H:%M:%S')}"
    