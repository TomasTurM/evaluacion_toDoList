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

        return redirect('/')

def delete_list_object(request, id_object):
    object = List_Object.objects.get(id=id_object)
    object.delete()
    return redirect('/')

def archive_list_object(request, id_object):
    object = List_Object.objects.get(id=id_object)
    object.archived = False
    object.save()

    return redirect('/')