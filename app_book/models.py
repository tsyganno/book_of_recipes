from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=50, verbose_name='Рецепт')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Рецепты'
        verbose_name = 'Рецепт'
        ordering = ['title']


class Ingredient(models.Model):
    name = models.CharField(max_length=50, verbose_name='Ингридиент')
    recipe = models.ManyToManyField(Recipe, related_name="ingr")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Ингридиенты'
        verbose_name = 'Ингридиент'
        ordering = ['name']
