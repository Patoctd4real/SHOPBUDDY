from django.shortcuts import render

# Create your views here.
def home(request):
    default_auto_field = 'django.db.models.AutoField'
    return render(request, 'home/home.html')
