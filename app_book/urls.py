from django.urls import path
from app_book.views import BaseView, RecipeView


app_name = 'book'
urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('recipe/<int:pk>/', RecipeView.as_view(), name='recipe'),
]
