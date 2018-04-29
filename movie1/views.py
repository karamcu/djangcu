
from django.http import Http404
from .models import Movie,Song
from django .shortcuts import render

def index(request):
	all_movies = Movie.objects.all()
	context={
		'all_movies':all_movies,
	}
	return render(request, 'movie1/index.html', context)

def detail(request, movie_id):
	try:
		m1=Movie.objects.get(pk=movie_id)
	except Movie.DoesNotExist:
		raise Http404("it is wrong hee haaa")
	return render(request, 'movie1/index1.html', {'m1':m1})

def favorite(request, movie_id):
	m1=Movie.objects.get(pk=movie_id)
	try:
		selected_song = m1.song_set.get(pk=request.POST['song'])

	except(KeyError, Song.DoesNotExist):
		return render(request, 'movie1/index1.html', {'m1': m1})
	else:
		selected_song.is_favorite=True
		selected_song.save()
		return render(request, 'movie1/index1.html', {'m1': m1})
# Create your views here.
