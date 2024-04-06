from django.shortcuts import render
from .models import MenuItem


def draw_menu(request, menu_name):
    menu_items: MenuItem = MenuItem.objects.filter(name=menu_name).select_related('parent')
    return render(request, 'tree_menu_app/index.html', {'menu_items': menu_items})
