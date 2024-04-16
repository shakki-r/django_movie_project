
from django.urls import path

from cart_movie import views
app_name='cart_movie'

urlpatterns = [

    path('add/',views.add_movie,name='add_movie'),
    path('my_movies/',views.my_movies,name='my_movies'),
    path('movie_info/<int:id>/',views.movie_details,name='movie_info'),
    path('edit_movie/<int:id>/',views.edit_movie,name='edit_movie'),
    path('delete_movie/<int:id>/',views.delete_movie,name='delete_movie'),
]