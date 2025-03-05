from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

'''
    two urls.py files: one in mysite folder, other in bookings.py folder
    bookings.py fodler contains urls for all webpages
'''
# for api
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'seats', SeatViewSet, basename='seat')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    # landing page will be movie list page
    path('', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/seats/', seat_booking, name='seat_booking'),
    path('bookings/history/', booking_history, name='booking_history'),
    path('api/', include(router.urls)),


]