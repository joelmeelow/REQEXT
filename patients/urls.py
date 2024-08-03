from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


from . import views


app_name = 'patients'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('search', views.search, name="search"),
    path('logout', views.logout, name="logout"),
   
    path('login/', views.login, name='login'),
    path('pharmverify/', views.pharmverify, name="pharmverify"),
    path('uploadimage/<int:pk>/', views.uploadimage, name='uploadimage'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset_confirm/uidb64/token/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
]


