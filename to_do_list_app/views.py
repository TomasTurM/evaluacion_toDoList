from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import *
from datetime import datetime

# Create your views here.

def list_render(request):
    context = {}
    context['list_objects'] = List_Object.objects.all()
    return render(request, 'list.html', context)

def save_list_object(request):
    if request.POST:
        content = request.POST.get('content', None)

        if content:
            new_object = List_Object()
            new_object.post_date = datetime.now().date()
            new_object.content = content
            new_object.archived = False

            new_object.save()

        return redirect('list_render')

def delete_list_object(request):
    object = List_Object.objects.get(id=request.POST.get('id'))
    object.delete()

    return redirect('list_render')

def archive_list_object(request):
    object = List_Object.objects.get(id=request.POST.get('id'))
    object.archived = True
    object.save()

    return redirect('list_render')