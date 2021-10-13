from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team


# Create your views here.

def demo(request):
    place_datas=Place.objects.all()
    team_datas=Team.objects.all()
    return render(request, 'index.html', {'place_datas': place_datas,'team_datas':team_datas})


def about(request):
    return render(request, 'about.html')


def add(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    result = x + y
    return render(request, 'result.html', {'result': result, 'x': x, 'y': y})
