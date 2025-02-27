from django.urls import path, include
from .views import *

'''
path('movies/', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/seats/', seat_booking, name='seat_booking'),
    path('bookings/history/', booking_history, name='booking_history'),


    two urls.py files: one in mysite folder, other in bookings.py folder
    bookings.py fodler contains urls for all webpages

    BRO THERES SOME WEIRD FUCKED UP SHIT HAPPENING WITH DEVEDU
    SOMETHING TO DO WITH THE HOST... https://editor-pdehoyos-5.devedu.io/proxy/
    INSTEAD OF http://127.0.0.1:8000/
    thats why my paths aren't working.... 
'''
urlpatterns = [
    # landing page will be movie list page
    path('', movie_list, name='movie_list'),
    #path('movies/', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/seats/', seat_booking, name='seat_booking'),
    path('bookings/history/', booking_history, name='booking_history'),

]