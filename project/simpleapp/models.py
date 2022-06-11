from django.db import models
from django.core.validators import MinValueValidator
 
  
class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    
    quantity = models.IntegerField(
        validators=[MinValueValidator(0, 'Quantity should be>=0')],
    )
    
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products', 
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0, 'Price should be>=0')],
    )
 
    def __str__(self):
        return f'{self.name.title()}: {self.quantity}'

    def get_absolute_url(self):
        return f'/products/{self.id}'
 
 

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  
 
    def __str__(self):
        return f'{self.name.title()}'
