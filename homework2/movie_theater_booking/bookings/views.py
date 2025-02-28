from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from .models import *


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def seat_booking(request, movie_id):
    # get the movie that was selected by user
    movie = Movie.objects.get(id=movie_id)
    # get all seats of the movie by using the movie's title
    seats = Seat.objects.filter(movie=movie)

    # for booking seats
    if request.method == "POST":
        # get the seat chosen by user
        seat_id = request.POST.get("seat_id")
        seat = Seat.objects.get(id=seat_id)

        # if seat is available
        if seat.seat_booking_status:
            # create booking 
            # user will be anonymous since not implementing login/authentication yet; so logic to include this
            Booking.objects.create(movie=movie, seat=seat, booking_user = request.user if request.user.is_authenticated else None, booking_date=now().date())
            # now that seat has been booked and tied to booking instance, make it unavailable
            seat.seat_booking_status = False
            seat.save()

            return redirect("booking_history")

        
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

def booking_history(request):
    bookings = Booking.objects.filter(booking_user=request.user.id)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
