from django.db import models

# Create your models here.

# Movie
class Movie(models.Model):
    # title
    movie_title = models.CharField(max_length=50)

    # description
    movie_desc = models.TextField()

    # release date
    # yyyy - mm - dd format; stores dates as python datetime.date
    movie_r_date = models.DateField()

    # duration
    movie_duration = models.DurationField()

# Seat
class Seat(models.Model):
    # seat number
    seat_number = models.IntegerField()

    # booking status
    seat_booking_status = models.BooleanField()


# Booking
class Booking(models.Model):
    # movie: many to one relationship; movies can have many bookings, but a booking can only have one movie. 
    # on_delete=models.CASCADE means if you delete a movie, its bookings will also be deleted. 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    # seat: many to one relationship; a booking can have multiple seats, but a seat can only be assigned to one booking. 
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    # user
    booking_user = models.CharField(max_length=50)

    # booking date
    booking_date = models.DateField()
