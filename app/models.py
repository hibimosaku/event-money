from unicodedata import category
from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
      return self.name

class CategoryMinor(models.Model):
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name

class Location(models.Model):
  name = models.CharField(max_length=50)
  gps = models.CharField(max_length=500,blank=True)

  def __str__(self):
      return self.name

class Event(models.Model):
  occurrence_date = models.DateField()
  category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
  category_minor = models.ForeignKey(CategoryMinor,on_delete=models.SET_NULL,null=True)
  content = models.CharField(max_length=100,blank=True)
  location = models.ForeignKey(Location,on_delete=models.SET_NULL,blank=True,null=True)
  ref_url = models.CharField(max_length=500,blank=True,null=True)
  price = models.IntegerField()

  def __str__(self):
      return self.category.name + ':' + self.occurrence_date
