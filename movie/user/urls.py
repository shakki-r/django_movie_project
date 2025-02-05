
from django.urls import path, include

from user import views
app_name='user'

urlpatterns = [

    path('',views.index,name='index'),
    path('genres/<slug>/', views.genres_filter, name='genres_filter'),

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit/<int:id>/',views.edit_profile,name='edit'),
    path('search/',views.search,name='search')
]
