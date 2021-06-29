
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [ 
    path('<str:chatid>/<str:incoming_message>/', index, name='index'),       
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

