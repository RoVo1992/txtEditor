from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'chat/index.html'


class RoomView(TemplateView):
    template_name = 'chat/room.html'


=======


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    print(request.user)
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
>>>>>>> 9069924 ("first commit")

