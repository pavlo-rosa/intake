from djongo import models

from djongo import models
from django import forms


class ListText(models.Model):
  text = models.CharField(max_length=255)

  class Meta:
    abstract = True


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


class IngredientItem(models.Model):
  ingredient = models.CharField(max_length=64)
  measure = models.CharField(max_length=64, null=True, blank=True)

  class Meta:
    abstract = True


class IngredientItemForm(forms.ModelForm):
  class Meta:
    model = IngredientItem
    fields = ('ingredient','measure')


class Recipe(models.Model):
  name = models.CharField(max_length=256)
  lang = models.CharField(max_length=256)

  ingredients = models.ArrayField(
    model_container=IngredientItem,
    model_form_class=IngredientItemForm
  )
  categories = models.ArrayField(
    model_container=Category
  )
  description = models.TextField()
  image = models.TextField()
  video = models.CharField(max_length=256)
  country = models.CharField(max_length=256)
  tags = models.ArrayField(
    model_container=ListText
  )

  def __str__(self):
    return str(self.id)+": "+ self.name
