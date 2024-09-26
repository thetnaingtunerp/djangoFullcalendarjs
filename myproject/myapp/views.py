from django.shortcuts import render

# Create your views here.
# calendarapp/views.py
# from django.shortcuts import render
from django.http import JsonResponse
from .models import Event

def calendar_view(request):
    return render(request, 'calendar.html')

def event_data(request):
    events = Event.objects.all()
    events_list = []
    for event in events:
        events_list.append({
            'title': event.title,
            'start': event.start.isoformat() if event.start else None,
            'end': event.end.isoformat() if event.end else None,
        })
    return JsonResponse(events_list, safe=False)
