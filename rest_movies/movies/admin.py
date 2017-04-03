from django.contrib import admin
from movies.models import Movie, Person, Role

# Register your models here.

admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Role)