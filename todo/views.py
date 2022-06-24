# pip3 install 'django<4'
# python3 manage.py runserver
# python3 manage.py makemigrations --dry-run
# python3 manage.py showmigrations
# python3 manage.py makemigrations --dry-plan
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py createsuperuser
# username: ckz8780, pantera101
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
