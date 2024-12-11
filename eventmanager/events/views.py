from django.shortcuts import render
from .models import Event


def event_list(request):
    list = Event.objects.all()
    return render(request,'events/event_list.html', {'list': list})
 
def add_event(request):
    return render(request,'events/add_event.html')
 
def edit_event(request):
    return render(request,'events/edit_event.html')

