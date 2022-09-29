from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'chat/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.GET)
        return context
    

class RoomView(TemplateView):
    template_name = 'chat/room1.html'



