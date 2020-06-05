from django.db import models

#Used to store title, URL of source, and URL of article image
class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()
    objects = models.Manager()
    
    #returns the string representation of fetched object
    def __str__(self):
        return self.title

#objects = models.Manager()
