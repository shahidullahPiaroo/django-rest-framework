from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# Method 3 : Model View Set

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename="book")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # Method 1 : APIView using class-based views

    # path('books/', views.BookListView.as_view()), # get, post request
    # path('books/<int:pk>/', views.BookListUpdateDelete.as_view()), # update, delete request

    # Method 2 : generic class-based views

    # path('books/', views.BookListCreateAPIView.as_view()), # get, post request handle
    # path('books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()), # update, delete request handle
    
    # Method 3 : Model View Set

    path('', include(router.urls)),
]