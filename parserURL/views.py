from django.shortcuts import render
from .models import Task

def home(request):

    return render(
        request,
        'home.html',
        context={'task_list':Task.objects.filter(is_done=True)},
    )

