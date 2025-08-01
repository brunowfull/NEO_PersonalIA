from django.shortcuts import render
from .models import UserInteraction

# View for displaying user interactions

def index(request):
    interactions = UserInteraction.objects.all()
    return render(request, 'index.html', {'interactions': interactions})
