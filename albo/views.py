from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Max
from albo.models import Team, Player, Competition, Game, Standings
from datetime import datetime

# Create your views here.
def index(request):
    trophies = Competition.objects.order_by('-date')
    comps_menu = Competition.objects.filter(date__year=datetime.now().year)
    return render(request, 'albo/albo.html', {'trophies': trophies, 'comps_menu': comps_menu})


def squadre(request):
    teams = Team.objects.order_by('name')
    comps_menu = Competition.objects.filter(date__year=datetime.now().year)
    return render(request, 'albo/rose.html', {'teams': teams, 'comps_menu': comps_menu})


def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    players = Player.objects.filter(team=team).order_by('toorder', 'name')
    trophies = Competition.objects.filter(winner=team).order_by('date')
    comps_menu = Competition.objects.filter(date__year=datetime.now().year)
    return render(request, 'albo/squadra.html', {'team': team, 'players': players, 'trophies': trophies, 'comps_menu': comps_menu})


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    comps_menu = Competition.objects.filter(date__year=datetime.now().year)
    return render(request, 'albo/partita.html', {'game': game, 'comps_menu': comps_menu})


def comps_all(request):
    comps = Competition.objects.order_by('date')
    comps_menu = Competition.objects.filter(date__year=datetime.now().year)
    return render(request, albo/comps_all.html, {'comps': comps, 'comps_menu': comps_menu})


def comp_detail(request, pk):
    comp = get_object_or_404(Competition, pk=pk)
    m = Standings.objects.filter(competition=comp).aggregate(Max('matchday'))['matchday__max']
    standings = Standings.objects.get(competition=comp, matchday=m)
    games = Game.objects.filter(competition=comp).order_by('matchday')
    comps_menu = Competition.objects.filter(date__year=datetime.now().year)
    return render(request, 'albo/comp.html', {'comp': comp, 'games': games, 'comps_menu': comps_menu, 'standings': standings})