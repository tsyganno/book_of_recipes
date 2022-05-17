from django.views.generic.base import TemplateView

from app_book.models import Recipe, Ingredient
from app_book.filters import RecipeFilter, IngredientFilter


def generation_recipe(id_recipe):
    return Recipe.objects.get(id=id_recipe)


def generation_ingredients(id_recipe):
    return Ingredient.objects.filter(recipe__id=id_recipe)


def all_ingredients():
    return [el.name for el in Ingredient.objects.all()]


class BaseView(TemplateView):
    template_name = 'layout/base.html'

    def get(self, request, *args, **kwargs):
        ingredients = all_ingredients()
        if 'title' in request.GET:
            if request.GET['title'] in all_ingredients():
                f = IngredientFilter(request.GET, Recipe.objects.filter(ingr__name__icontains=request.GET['title']).
                                     distinct())
                return self.render_to_response({'filter': f, 'ingredients': set(ingredients)})
        f = RecipeFilter(request.GET, Recipe.objects.all())
        return self.render_to_response({'filter': f, 'ingredients': set(ingredients)})


class RecipeView(TemplateView):
    template_name = 'app_book/recipe.html'

    def get(self, request, *args, **kwargs):
        if 'title' in request.GET:
            if request.GET['title'] in all_ingredients():
                f = IngredientFilter(request.GET, Recipe.objects.filter(ingr__name__icontains=request.GET['title']).
                                     distinct())
                recipe = generation_recipe(kwargs['pk'])
                ingredients_of_recipe = generation_ingredients(self.kwargs['pk'])
                return self.render_to_response({'filter': f, 'recipe': recipe, 'ingredients': ingredients_of_recipe})
        f = RecipeFilter(request.GET, queryset=Recipe.objects.all())
        recipe = generation_recipe(kwargs['pk'])
        ingredients_of_recipe = generation_ingredients(self.kwargs['pk'])
        return self.render_to_response({'filter': f, 'recipe': recipe, 'ingredients': ingredients_of_recipe})
