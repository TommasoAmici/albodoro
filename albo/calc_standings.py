from albo.models import *
comps = Competition.objects.filter(comp_format='season')
for c in comps:
    indices = Game.objects.filter(competition=c).order_by('-matchday').first()
    if indices:
        for i in range(1, indices+1):
            games = Game.objects.filter(competition=c, matchday=i)
            s = Standings(competition=c, matchday=m)
            for game in games:
                p0 = Position.objects.get(matchday=i-1, team=t0.team, competition=))
                p1 = Position.objects.create(matchday=i, team=t0.team, wins=w0))
                t0 = game.teams.all()[0]
                t1 = game.teams.all()[1]
                try:
                    w0 = 
                except:
                    w0 = 0
                try:
                    w1 = 
                except:
                    w0 = 0
                try:
                    l0 = 
                except:
                    w0 = 0
                try:
                    l1 = 
                except:
                    w0 = 0
                try:
                    d0 = 
                except:
                    w0 = 0
                try:
                    d1 = 
                except:
                    w0 = 0
                try:
                    gf0 = 
                except:
                    w0 = 0
                try:
                    gf1 = 
                except:
                    w0 = 0
                try:
                    ga0 = 
                except:
                    w0 = 0
                try:
                    ga1 = 
                except:
                    w0 = 0
                Position.objects.create(matchday=i, team=t0.team, wins=w0))

        
