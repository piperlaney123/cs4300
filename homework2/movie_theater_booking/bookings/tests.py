from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
from django.utils.timezone import now
from datetime import date


# Create your tests here.


class MovieModelTest(TestCase):

    def test_movie_creation(self):
        # Test if a movie is created successfully
        movie = Movie.objects.create(
            movie_title="Test Movie",
            movie_desc="This is a test description.",
            movie_r_date=date(2025, 3, 3),
            movie_duration=120
        )
        self.assertEqual(movie.movie_title, "Test Movie")
        self.assertEqual(movie.movie_desc, "This is a test description.")
        self.assertEqual(movie.movie_r_date, date(2025, 3, 3))
        self.assertEqual(movie.movie_duration, 120)
    
    def test_movie_creates_seats(self):
        # Test if 10 seats are created when a movie is saved
        movie = Movie.objects.create(
            movie_title="Test Movie",
            movie_desc="This is a test description.",
            movie_r_date=date(2025, 3, 3),
            movie_duration=120
        )
        self.assertEqual(movie.seats.count(), 10)

    def test_movie_str(self):
        # Test the string representation of the movie model 
        movie = Movie.objects.create(
            movie_title="Test Movie",
            movie_desc="Test description",
            movie_r_date=date(2025, 3, 3),
            movie_duration=120
        )
        self.assertEqual(str(movie), "Test Movie")


class SeatModelTest(TestCase):

    def test_seat_creation(self):
        # Test if a seat is correctly created and linked to a movie 
        movie = Movie.objects.create(
            movie_title="Test Movie",
            movie_desc="Test description",
            movie_r_date=date(2025, 3, 3),
            movie_duration=120
        )
        seat = movie.seats.first()
        self.assertIsNotNone(seat)
        self.assertEqual(seat.movie, movie)
        self.assertEqual(seat.seat_number, 1)
        self.assertTrue(seat.seat_booking_status)

    def test_seat_str(self):
        # Test the string representation of the seat model 
        movie = Movie.objects.create(
            movie_title="Test Movie",
            movie_desc="Test description",
            movie_r_date=date(2025, 3, 3),
            movie_duration=120
        )
        seat = movie.seats.first()
        self.assertEqual(str(seat), "1")


class BookingModelTest(TestCase):

    def test_booking_creation(self):
        # Test if a booking is successfully created 
        user = User.objects.create_user(username="testuser", password="password123")
        movie = Movie.objects.create(
            movie_title="Test Movie",
            movie_desc="Test description",
            movie_r_date=date(2025, 3, 3),
            movie_duration=120
        )
        seat = movie.seats.first()

        booking = Booking.objects.create(
            movie=movie,
            seat=seat,
            booking_user=user,
            booking_date=date(2025, 3, 3)
        )

        self.assertEqual(booking.movie, movie)
        self.assertEqual(booking.seat, seat)
        self.assertEqual(booking.booking_user, user)
        self.assertEqual(booking.booking_date, date(2025, 3, 3))

    def test_booking_seat_uniqueness(self):
        # Test that a seat cannot be booked twice!
        user1 = User.objects.create_user(username="user1", password="password123")
        user2 = User.objects.create_user(username="user2", password="password123")
        movie = Movie.objects.create(
            movie_title="Test Movie",
            movie_desc="Test description",
            movie_r_date=date(2025, 3, 3),
            movie_duration=120
        )
        seat = movie.seats.first()

        # First booking should be successful
        Booking.objects.create(
            movie=movie,
            seat=seat,
            booking_user=user1,
            booking_date=date(2025, 3, 3)
        )

        # Second booking should fail
        with self.assertRaises(Exception):  # Since seat is OneToOneField
            Booking.objects.create(
                movie=movie,
                seat=seat,
                booking_user=user2,
                booking_date=date(2025, 3, 3)
            )

    def test_booking_str(self):
        # Test the string representation of the booking model
        user = User.objects.create_user(username="testuser", password="password123")
        movie = Movie.objects.create(
            movie_title="Test Movie",
            movie_desc="Test description",
            movie_r_date=date(2025, 3, 3),
            movie_duration=120
        )
        seat = movie.seats.first()
        booking = Booking.objects.create(
            movie=movie,
            seat=seat,
            booking_user=user,
            booking_date=date(2025, 3, 3)
        )

        self.assertEqual(str(booking), "testuser")