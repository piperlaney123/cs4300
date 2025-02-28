from django.urls import path, include
from .views import *

'''
    two urls.py files: one in mysite folder, other in bookings.py folder
    bookings.py fodler contains urls for all webpages
'''
urlpatterns = [
    # landing page will be movie list page
    path('', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/seats/', seat_booking, name='seat_booking'),
    path('bookings/history/', booking_history, name='booking_history'),

]