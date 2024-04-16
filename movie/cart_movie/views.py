from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.text import slugify
from .models import Genres, Movies, Review
from django.contrib.auth.models import User

def add_movie(request):
    genres = Genres.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['poster']
        desc = request.POST['description']
        release_date = request.POST['release_date']
        actor = request.POST['actors']
        select_genres = request.POST['genres']
        gen = Genres.objects.get(genres=select_genres)
        youtube = request.POST['trailer_link']
        slug = slugify(title)
        username = request.user

        movie = Movies.objects.create(title=title, slug=slug, image=image, description=desc, release_date=release_date,
                                      actor=actor, genres=gen, youtube=youtube, added_user=username)
        movie.save()
        return redirect('cart_movie:my_movies')

    return render(request, 'add_movies.html', {'genres': genres})


def my_movies(request):
    user = request.user
    list_movie = Movies.objects.filter(added_user=user)

    return render(request, 'my_movies.html', {'list_movie': list_movie})


def movie_details(request, id):
    movie = Movies.objects.get(id=id)
    user = request.user
    review = None
    if request.method == 'POST':
        review = request.POST['review']
        rating = request.POST['rating']

        new_review = Review.objects.create(review=review, rating=rating, movie=movie, added_user=user)
        new_review.save()
        return redirect('cart_movie:movie_info', id=id)
    else:
        review = Review.objects.filter(movie__title=movie.title)

    return render(request, 'display_movie.html', {'movie': movie, 'user': user, 'review': review})

def edit_movie(request,id):
    movie=Movies.objects.get(id=id)

    genres=Genres.objects.all()
    if request.method=='POST':
        title = request.POST['title']
        try:

            image = request.FILES['poster']
        except MultiValueDictKeyError:
            image = movie.image

        try:
            release_date = request.POST['release_date']
        except KeyError:
            release_date = movie.release_date


        desc = request.POST['description']
        actor = request.POST['actors']
        select_genres = request.POST['genres']
        gen = Genres.objects.get(genres=select_genres)
        youtube = request.POST['trailer_link']
        slug = slugify(title)
        username = request.user

        movie.title=title
        movie.image=image
        movie.description=desc
        movie.actor=actor
        movie.release_date=release_date
        movie.genres=gen
        movie.youtube=youtube
        movie.save()
        return redirect('cart_movie:movie_info',id=id)




    return render(request,'edit_movie.html',{'movie':movie,'genres':genres})


def delete_movie(request,id):
    movie=Movies.objects.get(id=id)
    movie.delete()
    return redirect('/')