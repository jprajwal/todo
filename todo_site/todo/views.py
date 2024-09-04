from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

# import todo form and models

from .forms import TodoForm
from .models import Todo


class TodoView(View):
    def get(self, request):
        form = TodoForm()
        item_list = Todo.objects.order_by("-date")
        page = {
            "forms": form,
            "list": item_list,
            "title": "TODO LIST",
        }
        return render(request, 'todo/index.html', page)

    def post(self, request):
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.info(request, "invalid information provided")
        return redirect('todo')


class TodoDeleteByIdView(View):
    def post(self, request, item_id):
        item = Todo.objects.get(id=item_id)
        item.delete()
        messages.info(request, "item removed !!!")
        return redirect('todo')


class HomeView(View):
    def get(self, request):
        return redirect('login')
