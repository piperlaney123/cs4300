from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Movie
class Movie(models.Model):
    # title
    movie_title = models.CharField(max_length=50)
    # description
    movie_desc = models.TextField()
    # release date
    # yyyy - mm - dd format; stores dates as python datetime.date (for testing with shell, from datetime import date; date(year, month, day))
    movie_r_date = models.DateField()
    # duration
    movie_duration = models.IntegerField()

    # for printing & testing
    def __str__(self):
        return self.movie_title

    # overriding save method to make sure once a movie is added, it also gets 10 seats added.
    # this is the only way this model architecture makes sense to me. every movie has 10 seats, but each seat is specific to that movie
    # exp: movie X has seats X1, X2, X3 .... movie Y has seats Y1, Y2, Y3 .... 
    # keep in mind when querying have to provide both seat number and movie name in case MulitpleObjectsReturned error gets thrown;
    # but this is kind of obvious. 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.seats.exists():
            for i in range(1, 11):
                Seat.objects.create(movie = self, seat_number = i, seat_booking_status = True)

# Seat
class Seat(models.Model):
    # movie seat
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats")
    # seat number
    seat_number = models.IntegerField()
    # booking status; True = seat is available
    seat_booking_status = models.BooleanField(default = True)

    # for printing & testing
    def __str__(self):
        return str(self.seat_number)


# Booking
class Booking(models.Model):
    # movie: many to one relationship; movies can have many bookings, but a booking can only have one movie. 
    # on_delete=models.CASCADE means if you delete a movie, its bookings will also be deleted. 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name = "bookings")
    # seat: one to one relationship, because a booking can only have one seat, and a seat can only be booked by one book (avoid duplicate books
    # for one seat at a movie theater)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE, related_name="booking")
    # user, using djangos built in user model
    booking_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # booking date
    booking_date = models.DateField()

    # for printing & testing
    def __str__(self):
        return self.booking_user.username
