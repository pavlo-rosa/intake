from djongo import models

from djongo import models
from django import forms


class LangText(models.Model):
  name = models.CharField(max_length=255)
  lang = models.CharField(max_length=3)

  class Meta:
    abstract = True


class Category(models.Model):
  category = models.ArrayField(
    model_container=LangText
  )

  def __str__(self):
    return str(self.id) + " - " + self.category[0].name if len(self.category) > 0 else str(self.id)

# class Recipe(models.Model)