from .models import Person, Movie
from .serializers import PersonSerializer, MovieSerializer
from django.http import Http404
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class MoviesView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)


class MovieView(APIView):

    def get_object(self, id):
        try:
            return Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)

    def delete(self, request, id):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data = request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)