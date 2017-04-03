from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name='director')
    actors = models.ManyToManyField(Person, through='Role')
    year = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.title,self.year)


class Role(models.Model):
    actor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='actor')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=128)

    def __str__(self):
        return "{} as {}".format(self.actor, self.role)


