from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from albo.models import Team, Player, Competition, Game

# Create your views here.
def index(request):
    trophies = Competition.objects.order_by('-date')
    return render(request, 'albo/albo.html', {'trophies': trophies})


def squadre(request):
    teams = Team.objects.order_by('name')
    return render(request, 'albo/rose.html', {'teams': teams})


def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    players = Player.objects.filter(team=team)
    trophies = Competition.objects.filter(winner=team)
    return render(request, 'albo/squadra.html', {'team': team, 'players': players, 'trophies': trophies})


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'albo/partita.html', {'game': game})


def comps_all(request):
    comps = Competition.objects.order_by('date')
    return render(request, albo/comps_all.html, {'comps': comps})


def comp_detail(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    games = Game.objects.filter(competition=comp).order_by('matchday')
    return render(request, 'albo/comp.html', {'comp': comp, 'games': games})