from django.urls import path
from . import views

app_name = 'care'


urlpatterns = [
    path('<int:pk>/', views.index, name="index"),
    path('inbox/<int:pk>/', views.inbox, name="inbox"),
    path('phar/<int:pk>/', views.phar, name="phar"),
    path('send/', views.send, name="send"),
   
    path('getMessages/<str:pk>/', views.getMessages, name='getMessages'),
    path('messageapi/', views.messageapi, name="massageapi")
   
]