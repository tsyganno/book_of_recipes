from django.contrib import admin
from app_book.models import Recipe, Ingredients


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredients)
