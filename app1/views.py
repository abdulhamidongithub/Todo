from django.shortcuts import render
from django.views import View
from .models import *


class TodoView(View):
    def get(self, request):
        content = {
            "todos": Plan.objects.all()
        }
        return render(request, 'todo.html', content)
