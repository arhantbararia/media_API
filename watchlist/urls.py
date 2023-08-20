from django.urls import path, include
#from .views import movie_list, movie_detail

app_name = 'watchlist'

urlpatterns = [
    path("api/" , include('watchlist.api.urls' , namespace="watchlist")),    
    
]





