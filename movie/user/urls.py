
from django.urls import path, include

from user import views
app_name='user'

urlpatterns = [

    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
]
