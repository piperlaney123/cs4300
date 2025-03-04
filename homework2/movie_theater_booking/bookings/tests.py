from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
from django.utils.timezone import now
from datetime import date
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import *

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


# test api endpoints 
class PostViewTestCase(APITestCase):
    def setUp(self):
        # set up & create models
        
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.movie = Movie.objects.create(movie_title="Test Movie", movie_desc="A test movie description", movie_r_date="2025-01-01", movie_duration=120)
        self.seat = Seat.objects.create(movie=self.movie, seat_number=11, seat_booking_status=True)
        self.booking = Booking.objects.create(movie=self.movie,seat=self.seat,booking_user=self.user,booking_date="2025-01-01")
        
        # endpoints
        self.movie_list_url = "/api/movies/"
        self.book_seat_url = "/api/seat/book_seat"
        self.booking_history_url = "/api/bookings/history"
        self.movie_update_url = f"/api/movies/{self.movie.id}/" # also for deleting...

    
    # testing time: movie
    # get
    def test_get_movie(self):
        response = self.client.get(self.movie_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]["movie_title"], "Test Movie")
        serializer_data = MovieSerializer([self.movie], many=True).data
        self.assertEqual(response.data, serializer_data)
    
    # post
    def test_create_movie(self):
        data = {
            "movie_title": "New Movie",
            "movie_desc": "This is a new test movie.",
            "movie_r_date": "2025-06-01",
            "movie_duration": 150
        }

        response = self.client.post(self.movie_list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check if movie was created
        self.assertEqual(response.data["movie_title"], "New Movie")  # Verify correct data
        self.assertEqual(Movie.objects.count(), 2)  # make sure movie was created, 2 b/c we already created a movie in past 

    # put/update
    def test_update_movie(self):
        data = {
            "movie_title": "Updated New Movie",
            "movie_desc": "Updated This is a new test movie.",
            "movie_r_date": "2024-06-01",
            "movie_duration": 130
        }

        response = self.client.put(self.movie_update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["movie_title"], "Updated New Movie")
        self.assertEqual(response.data["movie_desc"], "Updated This is a new test movie.")
        self.assertEqual(response.data["movie_r_date"], "2024-06-01")
        self.assertEqual(response.data["movie_duration"], 130)

    # delete
    def test_delete_post(self):
        response = self.client.delete(self.movie_update_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=self.movie.id).exists())

    # testing time: book seats