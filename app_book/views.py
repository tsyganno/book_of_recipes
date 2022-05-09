from django.shortcuts import render
from django.views.generic.base import TemplateView

from app_book.models import Recipe, Ingredients


class BaseView(TemplateView):
    template_name = 'layout/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.all()
        return context


class RecipeView(TemplateView):
    template_name = 'app_book/recipe.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeView, self).get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.get(id=self.kwargs['pk'])
        context['ingredients'] = Ingredients.objects.filter(recipe__id=self.kwargs['pk'])
        return context

