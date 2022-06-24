from django.db import models

# Create your models here.


class Category(models.Model):
    placementId = models.PositiveIntegerField(default=1,blank=False,null=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['placementId']
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __str__(self) -> str:
        return str(self.name)
    
     
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField( null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name

