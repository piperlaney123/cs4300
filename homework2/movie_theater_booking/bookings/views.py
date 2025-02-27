from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def seat_booking(request, movie_id):
    # get the movie that was selected by user
    movie = Movie.objects.get(id=movie_id)
    # get all seats of the movie by using the movie's title
    seats = Seat.objects.all(movie = movie.movie_title)

    if request.method == "POST":
        # get the seat chosen by user
        seat_id = request.POST.get("seat_id")
        seat = Seat.objects.get(id=seat_id)

        # if seat is available
        if seat.seat_booking_status:
            # update booking with seat 
            # MIGHT HAVE TO DO MORE WITH THIS FOR BOOKING - UPDATE MOVIE, USER, BOOKING DATE...
            Booking.objects.create(user=request.user, movie=movie).seat.add(seat)
            # make seat unavailable
            seat.seat_booking_status = False
            # save to database
            seat.save()
        
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
