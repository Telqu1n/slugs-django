from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Food
from django.shortcuts import get_object_or_404

# Create your views here.

class IndexView(TemplateView):
    template_name = 'slug_app/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Food'] = Food.objects.all()
        return context
      

class FoodDetailView(TemplateView):
    template_name = 'slug_app/details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')  # Get slug from URL
        food = get_object_or_404(Food, slug=slug)
        context['food'] = food  # Assign the 'food' object here
        return context