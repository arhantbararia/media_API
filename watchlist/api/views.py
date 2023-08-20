
from django.core.exceptions import ValidationError

from watchlist.models import Media, StreamPlatform, Review, Country, Language


from .serializers import MediaSerializer, StreamPlatformSerializer, ReviewSerializer, GetMediaSerializer, CountrySerializer , LanguageSerializer

from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.permissions import IsAdminUser , IsAuthenticated , IsAuthenticatedOrReadOnly

from .permissions import AdminOrReadOnly , AuthorOrReadOnly


class CountryListAV(APIView):
    def get(self, request ):
        country = Country.objects.all()
        serializer = CountrySerializer(country , many = True)

        return Response(serializer.data)
    

class CountryDetailAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get_object(self, primaryKey):
        try:
            return Country.objects.get(pk = primaryKey)

        except Country.DoesNotExist:
            print("Error Here!")
            return Response({'ERROR' : 'Object Does not exist'} , status = status.HTTP_404_NOT_FOUND)
        

    def get(self, request ,CountryID):
        country = self.get_object(CountryID )

        serializer = CountrySerializer(country)
        return Response(serializer.data)
    

    def put(self, request , CountryID):
        country = self.get_object(CountryID)
        serializer = CountrySerializer(country , data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, primaryKey):
        country = self.get_object(primaryKey)
        country.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
    

class LanguageListAV(APIView):
    def get(self, request ):
        language = Language.objects.all()
        serializer = LanguageSerializer(language , many = True)

        return Response(serializer.data)
    

class LanguageDetailAV(APIView):
    permission_classes = [AdminOrReadOnly]

    def get_object(self, primaryKey):
        try:
            return Language.objects.get(pk = primaryKey)

        except Language.DoesNotExist:
            print("Error Here!")
            return Response({'ERROR' : 'Object Does not exist'} , status = status.HTTP_404_NOT_FOUND)
        

    def get(self, request ,LanguageID):
        language = self.get_object(LanguageID )

        serializer = LanguageSerializer(language)
        return Response(serializer.data)
    

    def put(self, request , LanguageID):
        language = self.get_object(LanguageID)
        serializer = LanguageSerializer(language , data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, primaryKey):
        language = self.get_object(primaryKey)
        language.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)





class CreateReviewAV( generics.CreateAPIView):
    
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer ):
        
        review_user = self.request.user

        
        
        primaryKey = self.kwargs['mediaId']
        
        media = Media.objects.get(pk = primaryKey)
        
        review_query_set = Review.objects.filter(media= media, author = review_user)
        
        if review_query_set.exists():
            raise ValidationError(f"Review from {review_user} for this movie already exists")
        
    
        if media.no_of_ratings == 0:
            media.avg_rating = serializer.validated_data['rating']
        else:
            media.avg_rating = (media.avg_rating  + serializer.validated_data['rating'])/2
        
        media.no_of_ratings += 1

        media.save()

        
        serializer.save(media = media , author = review_user)
            
    

class ReviewListAV( mixins.ListModelMixin, generics.GenericAPIView ):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        
        mediaID = self.kwargs['mediaId']
        return Review.objects.filter(media = mediaID)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
    

class ReviewAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [AuthorOrReadOnly]
    
    def get_queryset(self):
        review_pk = self.kwargs['pk']
        return Review.objects.filter(pk = review_pk)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    






class MediaListAV(APIView):
    
    permission_classes = [AdminOrReadOnly]
    
    def get(self, request):
        medias = Media.objects.all()
        serializer = GetMediaSerializer(medias , many = True )

        return Response(serializer.data)
    

    def post(self, request):
        serializer = MediaSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    


class MediaAV(APIView):
    
    permission_classes = [AdminOrReadOnly]

    def get_object(self, primaryKey):
        try:
            return Media.objects.get(pk = primaryKey)

        except Media.DoesNotExist:
            print("Error Here!")
            return Response({'ERROR' : 'Object Does not exist'} , status = status.HTTP_404_NOT_FOUND)
        

    def get(self, request ,primaryKey):
        media= self.get_object(primaryKey )

        serializer = GetMediaSerializer(media)
        return Response(serializer.data)
    

    def put(self, request , primaryKey):
        media = self.get_object(primaryKey)
        serializer = MediaSerializer(media , data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, primaryKey):
        media = self.get_object(primaryKey)
        media.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)

    
class PlatformListAV(APIView):
    permission_classes = [AdminOrReadOnly]
    lookup_field='id'
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms , many = True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):

        serializer = StreamPlatformSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    

class PlatformAV(APIView):

    lookup_field='id'
    permission_classes = [AdminOrReadOnly]

    def get_object(self, primaryKey):
        try:
            return StreamPlatform.objects.get(pk = primaryKey)

        except Media.DoesNotExist:
            print("Error Here!")
            return Response({'ERROR' : 'Object Does not exist'} , status = status.HTTP_404_NOT_FOUND)
        
    def get(self, request, primaryKey):
        platform = self.get_object(primaryKey)
        serializer = StreamPlatformSerializer(platform , context = {'request' : request})

        return Response(serializer.data)
    
    def put(self, request , primaryKey):
        platform = self.get_object(primaryKey)
        serializer = StreamPlatformSerializer(platform)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, primaryKey):
        platform = StreamPlatform.objects.get(pk = primaryKey)
        platform.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)

    
    







# @api_view(['GET'])
# @permission_classes([isAdmin])
# def getMovies(request):
#     movies = Movie.objects.all()
#     serializer = MediaSerializer(movies , many = True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def createMovie(request):
#     serializer = MediaSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
    

# @api_view(['GET' , 'PUT' , 'DELETE'])
# def getMovie(request , primaryKey):
    

#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk = primaryKey)
#         except Movie.DoesNotExist:
#             return Response({'error' : 'Movie Not Found'} , status = status.HTTP_404_NOT_FOUND)
#         serializer = MediaSerializer(movie)
#         print(serializer.data)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk = primaryKey)
    
#         serializer = MediaSerializer( movie , data = request.data )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk = primaryKey)
#         movie.delete()

#         return Response(status= status.HTTP_204_NO_CONTENT)
    

        

    
