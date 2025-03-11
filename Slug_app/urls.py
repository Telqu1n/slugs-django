from django.urls import path
from .views import IndexView, FoodDetailView

urlpatterns = [
    path('', IndexView.as_view()),
    path ('details/<slug:slug>/', FoodDetailView.as_view(), name='food_detail'),
]