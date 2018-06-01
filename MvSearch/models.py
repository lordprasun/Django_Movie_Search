from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100)
    imdb_score = models.CharField(max_length=10)
    popularity99 = models.CharField(max_length=10)
    director = models.CharField(max_length=100)
    genre =  models.CharField(max_length=200)
    def __str__(self):
        return self.name + " " + str(self.imdb_score)\
               + " " + str(self.popularity99)+ " " \
               + self.director+ " " + self.genre