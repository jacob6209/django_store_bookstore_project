from django.db import models

class book(models.Model):
     title=models.CharField(max_length=200)
     author=models.CharField(max_length=200)
     content=models.TextField
     price=models.DecimalField(max_digits=5,decimal_places=2) # For Mony Use => Decimal Field
     def __str__(self):
          return self.title
