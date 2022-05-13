from app_book.models import Ingredient, Recipe
import django_filters


class RecipeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact', label='Рецепты')

    class Meta:
        model = Recipe
        fields = ['title']


class IngredientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact', label='Рецепты')

    class Meta:
        model = Ingredient
        fields = ['name']
