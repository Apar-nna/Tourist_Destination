# destinations/urls.py

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import DestinationViewSet
#
# router = DefaultRouter()
# router.register(r'destinations', DestinationViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

# destinations/urls.py

# destinations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('add/', views.add_destination, name='add_destination'),
    path('update/<int:id>/', views.update_destination, name='update_destination'),
    path('delete/<int:id>/', views.delete_destination, name='delete_destination'),
]


