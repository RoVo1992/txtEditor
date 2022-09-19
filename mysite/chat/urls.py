from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.IndexView.as_view(), name='index'),
                  path('chat/<str:room_name>/', views.RoomView.as_view(), name='room'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
