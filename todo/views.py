# python3 manage.py runserver
# python3 manage.py makemigrations --dry-run
# python3 manage.py showmigrations
# python3 manage.py makemigrations --dry-plan
# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py createsuperuser
# username: ckz8780, pantera101
from django.shortcuts import render
from .models import Item

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "todo/todo_list.html", context)
