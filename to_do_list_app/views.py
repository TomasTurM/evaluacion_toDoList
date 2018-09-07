from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def list_render(request):
    context = {}
    context['list_objects'] = List_Object.objects.all()
    return render(request, 'list.html', context)

def save_list_object(request):
    if request.POST:
        post_date = request.POST.get('post_date', None)
        content = request.POST.get('content', None)
        archived = request.POST.get('archived', None)

        if content:
            new_object = List_Object()
            new_object.post_date = post_date
            new_object.content = content
            new_object.archived = archived

        return redirect('/')

def delete_object(request, id_object):
    object = List_Object.objects.get(id=id_object)
    object.delete()
    return redirect('/')

def archive_object(request, id_object):
    object = List_Object.objects.get(id=id_object)
    object.archived = True
    return redirect('/')