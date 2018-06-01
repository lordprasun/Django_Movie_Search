import json
from django.shortcuts import render,redirect
from .models import Member
from django.db.models import Q

def index_redirect(request):
    return redirect('/MvSearch/')

def index(request):
    members = Member.objects.all().order_by('name')
    return render(request, 'MvSearch/index.html', {'members': members})

def create(request):
    jsonfile = request.POST['jsonfile']
    mvdata = json.load(open(jsonfile))
    for movies in mvdata:
        member = Member(name = movies['name'],
                        imdb_score = movies['imdb_score'],
                        popularity99 = movies['99popularity'],
                        director = movies['director'],
                        genre = movies['genre'],)
        member.save()
    return redirect('/')
def search(request):
    members = Member.objects.filter(Q(name=request.GET.get('search')) | Q(imdb_score=request.GET.get('search'))
                                    | Q(popularity99=request.GET.get('search'))
                                    | Q(director=request.GET.get('search'))
                                    | Q(genre=request.GET.get('search')))
    return render(request, 'MvSearch/index.html', {'members': members})