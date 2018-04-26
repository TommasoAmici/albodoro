# calculates final score for a game
from albo.models import *
games = Game.objects.all()
for game in games:
    for team in game.teams.all():
        fp = 0
        for p in team.players.filter(bench=0):
            if p.fantavote is None:
                continue
            else:
                fp += p.fantavote
        team.fantapunti = fp
        team.save()
        team.goals = 0
        if fp >= 66:
            team.goals = (fp-62)//4
        team.save()