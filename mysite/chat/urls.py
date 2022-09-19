from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
                  path('', views.IndexView.as_view(), name='index'),
                  path('chat/<str:room_name>/', views.RoomView.as_view(), name='room'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

>>>>>>> 9069924 ("first commit")
