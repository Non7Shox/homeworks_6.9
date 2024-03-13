from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def themes_list(request):
    with open('Themes/Lessons.txt', 'r') as file:
        themes = file.readlines()
    return HttpResponse(themes)


from django.shortcuts import render


def pupils_list(request):
    pupils = [
        {'id': 1, 'name': 'John', 'grade': 'A'},
        {'id': 2, 'name': 'Alice', 'grade': 'B'},
        {'id': 3, 'name': 'Bob', 'grade': 'C'},
        {'id': 4, 'name': 'Emma', 'grade': 'A'},
        {'id': 5, 'name': 'Michael', 'grade': 'B'},
    ]
    return render(request, 'pupils_list.html', {'pupils': pupils})


def pupil_detail(request, id):
    pupil = {'id': id, 'name': 'John Doe', 'grade': 'A+'}
    return render(request, 'pupil_detail.html', {'pupil': pupil})
