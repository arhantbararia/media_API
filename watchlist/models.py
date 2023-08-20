from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class Language(models.Model):
    language = models.CharField(max_length = 20)

    def __str__(self):
        return self.language




class Country(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

class StreamPlatform(models.Model):
    name = models.CharField(max_length = 20)
    website = models.URLField(max_length= 100 )
    #countries = models.ManyToManyField(Country)


    def __str__(self):
        return self.name
    
def rating_range_assertion(value):
    if(value <= 5) and (value >= 1):
        return value
    else:
        raise ValidationError("Rating must be within range 1 to 5")




# Create your models here.
class Media(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.CharField(max_length= 200)
    released = models.BooleanField( verbose_name= 'Released' ,default=True)
    
    avg_rating = models.FloatField(default = 0)
    no_of_ratings = models.IntegerField(default = 0)


    language = models.ForeignKey(Language, on_delete=models.CASCADE, default = 3)

    platforms = models.ManyToManyField(StreamPlatform , related_name="media")
    country = models.ManyToManyField(Country, related_name = "media")


    def __str__(self):
        return f"{self.title}  -  {self.year}"
    

class Review(models.Model):
    
    author = models.ForeignKey(User, on_delete= models.CASCADE)


    rating = models.PositiveIntegerField(validators=[rating_range_assertion])
    description = models.CharField(max_length= 200)
    media = models.ForeignKey(Media , on_delete=models.CASCADE, related_name="review")

    active = models.BooleanField(default = True)

    

    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author.username} - {self.rating} - {self.description} - Movie: {self.media.title}"
