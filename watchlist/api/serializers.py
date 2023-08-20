from rest_framework import serializers
from watchlist.models import Media, StreamPlatform, Review, Language, Country

from datetime import date



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
        


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = "__all__"
    





class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Review
        #fields = "__all__"
        exclude = ('media',)


class GetMediaSerializer(serializers.ModelSerializer):
    

    
    review = serializers.StringRelatedField(many = True, read_only = True)
    platforms = serializers.StringRelatedField(many = True, read_only = True)
    language = serializers.StringRelatedField()
    country = serializers.StringRelatedField(many = True)


    class Meta:
        model = Media
        fields = "__all__" 
        #('id' , 'title', 'year', 'description' , 'released', 'StreamPlatform')
        
    
    

class MediaSerializer(serializers.ModelSerializer):
    

   
    review = serializers.StringRelatedField(many = True, read_only = True)
    platforms = serializers.StringRelatedField(many = True, read_only = True)
    # language = serializers.StringRelatedField()
    # country = serializers.StringRelatedField(many = True)
    

    class Meta:
        model = Media
        fields = "__all__" 
        #('id' , 'title', 'year', 'description' , 'released', 'StreamPlatform')
        
    
    def validate(self , data):
        if (int(data["year"]) >  int(date.today().year)) and (data['released'] == True):
            raise serializers.ValidationError( "Released Movie cannot have year >  Current year" ) 
        else:
            return data   


class StreamPlatformSerializer(serializers.ModelSerializer):
    
    
    media = serializers.StringRelatedField(many= True)
    #media = serializers.HyperlinkedRelatedField(many = True, 
      #                                          read_only = True ,view_name = 'Media-detail')
    # url = serializers.HyperlinkedIdentityField(view_name="StreamPlatform-detail" ) 
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        

    #media = MediaSerializer(many = True, read_only = True)
    #media = serializers.StringRelatedField(many= True)
                                               
    




# def check_name_length(value):
#     if(len(value) < 2 ):
#         raise serializers.ValidationError("Movie name must be greater than 2")
    

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators = [check_name_length])
#     year = serializers.CharField()
#     description = serializers.CharField()

#     released = serializers.BooleanField()

#     def create(self , validated_data):
#         return Movie.objects.create(**validated_data)
    

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name' , instance.name)
#         instance.year = validated_data.get('year' , instance.year)
#         instance.description = validated_data.get('description' , instance.description)
#         instance.released = validated_data.get('released' , instance.released)
#         instance.save()

#         return instance
    
        
    
#     def validate(self, data):
#         if (int(data["year"]) >  int(date.today().year)) and (data['released'] == True):
#             raise serializers.ValidationError( "Released Movie cannot have year >  Current year" ) 
#         else:
#             return data
    