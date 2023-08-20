from django.urls import path

#from .views import getMovies, getMovie
from .views import MediaListAV, MediaAV, PlatformListAV, PlatformAV, ReviewListAV, CreateReviewAV,  ReviewAV, LanguageListAV, LanguageDetailAV, CountryListAV, CountryDetailAV


app_name = 'watchlist'


urlpatterns = [
    
    path("getMedia/" , MediaListAV.as_view() , name= 'Media-list'),    
    path('getMedia/<int:primaryKey>', MediaAV.as_view() , name = 'Media-detail' ),
    
    path('getMedia/<int:mediaId>/create-review' , CreateReviewAV.as_view(), name= 'create-movie-review' ),
    path('getMedia/<int:mediaId>/reviews', ReviewListAV.as_view() , name = 'Movie-review-list' ),
    path('getMedia/review/<int:pk>' , ReviewAV.as_view(), name='review-detail'),


    path("platforms/",  PlatformListAV.as_view(), name = "StreamPlatform-list"),
    path("platform/<int:primaryKey>" , PlatformAV.as_view() , name = "StreamPlatform-detail"),
    
    path("languages/" , LanguageListAV.as_view() , name = "Languages List" ),
    path("language/<int:languageID>" , LanguageDetailAV.as_view(), name = "Language Detail"),

    path("countries/" , CountryListAV.as_view() , name = "Countries"),
    path("country/<int:countryID>" , CountryDetailAV.as_view() ,name = "Country Detail"),


 
]



# urlpatterns = [
#     path("getMovies/" , getMovies , name= 'movie-list'),    
#     path('getMovie/<int:primaryKey>', getMovie , name = 'movie_detail' ),
# ]