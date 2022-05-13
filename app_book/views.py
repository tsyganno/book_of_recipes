from django.views.generic.base import TemplateView

from app_book.models import Recipe, Ingredient
from app_book.filters import RecipeFilter, IngredientFilter


def generation_list_ingredient():
    ingredient_list = []
    for el in Ingredient.objects.all():
        ingredient_list.append(el.name)
    return ingredient_list


class BaseView(TemplateView):
    template_name = 'layout/base.html'

    def get(self, request, *args, **kwargs):
        ingredients = []
        for el in Ingredient.objects.all():
            ingredients.append(el.name)
        if 'title' in request.GET:
            if request.GET['title'] in generation_list_ingredient():
                f = IngredientFilter(request.GET, Recipe.objects.filter(ingr__name__icontains=request.GET['title']).
                                     distinct())
                return self.render_to_response({'filter': f, 'ingredients': set(ingredients)})
        f = RecipeFilter(request.GET, Recipe.objects.all())
        return self.render_to_response({'filter': f, 'ingredients': set(ingredients)})


class RecipeView(TemplateView):
    template_name = 'app_book/recipe.html'

    def get(self, request, *args, **kwargs):
        if 'title' in request.GET:
            if request.GET['title'] in generation_list_ingredient():
                f = IngredientFilter(request.GET, Recipe.objects.filter(ingr__name__icontains=request.GET['title']).
                                     distinct())
                recipe = Recipe.objects.get(id=self.kwargs['pk'])
                ingredients = Ingredient.objects.filter(recipe__id=self.kwargs['pk'])
                return self.render_to_response({'filter': f, 'recipe': recipe, 'ingredients': ingredients})
        f = RecipeFilter(request.GET, queryset=Recipe.objects.all())
        recipe = Recipe.objects.get(id=self.kwargs['pk'])
        ingredients = Ingredient.objects.filter(recipe__id=self.kwargs['pk'])
        return self.render_to_response({'filter': f, 'recipe': recipe, 'ingredients': ingredients})
