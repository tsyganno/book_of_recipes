from django.views.generic.base import TemplateView

from app_book.models import Recipe, Ingredient
from app_book.filters import RecipeFilter, IngredientFilter


class BaseView(TemplateView):
    template_name = 'layout/base.html'

    def get(self, request, *args, **kwargs):
        ingredients = set([el.name for el in Ingredient.objects.all()])
        if 'title' in request.GET:
            if request.GET['title'] in ingredients:
                ingredient_filter = IngredientFilter(request.GET, Recipe.objects.filter(ingr__name__icontains=request.
                                                                                        GET['title']).distinct())
                return self.render_to_response({'filter': ingredient_filter, 'ingredients': ingredients})
        recipe_filter = RecipeFilter(request.GET, Recipe.objects.all())
        return self.render_to_response({'filter': recipe_filter, 'ingredients': ingredients})


class RecipeView(TemplateView):
    template_name = 'app_book/recipe.html'

    def get(self, request, *args, **kwargs):
        ingredients = set([el.name for el in Ingredient.objects.all()])
        recipe = Recipe.objects.get(id=kwargs['pk'])
        ingredients_of_recipe = Ingredient.objects.filter(recipe__id=self.kwargs['pk'])
        if 'title' in request.GET:
            if request.GET['title'] in ingredients:
                ingredient_filter = IngredientFilter(request.GET, Recipe.objects.filter(ingr__name__icontains=request.
                                                                                        GET['title']).distinct())
                return self.render_to_response({'filter': ingredient_filter, 'recipe': recipe,
                                                'ingredients': ingredients_of_recipe})
        recipe_filter = RecipeFilter(request.GET, queryset=Recipe.objects.all())
        return self.render_to_response({'filter': recipe_filter, 'recipe': recipe,
                                        'ingredients': ingredients_of_recipe})
