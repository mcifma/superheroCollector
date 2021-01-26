from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

superheroes = ["Super Man", "Bat Man", "Wonder Woman", "Black Widow"]

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to the My Superheroes Collection</h1>')

def about(request):
  return render(request, 'about.html')

def superheroes_index(request):
  return render(request, 'superheroes/index.html', { 'superheroes': superheroes })