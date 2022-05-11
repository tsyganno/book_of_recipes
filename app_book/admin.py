from django.contrib import admin
from app_book.models import Recipe, Ingredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
