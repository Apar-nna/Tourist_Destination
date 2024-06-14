from django.db import models

class Destination(models.Model):
    place_name = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    district = models.CharField(max_length=100)  # Define district field
    state = models.CharField(max_length=100)     # Define state field
    google_map_link = models.URLField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.place_name
