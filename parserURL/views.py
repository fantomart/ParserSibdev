from django.shortcuts import render
from .models import Task

def get_all_done_tasks():
    return Task.objects.filter(is_done=True)

def home(request):

    return render(
        request,
        'home.html',
        context={'task_list':get_all_done_tasks(),
                'results_list':get_all_done_tasks()},
    )

