from django.shortcuts import render

# Create your views here.
# allows us to render the index file from templates directory
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')