from albo.models import *
comps = Competition.objects.filter(comp_format='season')
for c in comps:
    indices = Game.objects.filter(competition=c).order_by('-matchday').first()
    if indices:
        for i in range(1, indices.matchday + 1):
            games = Game.objects.filter(competition=c, matchday=i)
            s = Standings.objects.create(competition=c, matchday=i)
            for game in games:
                t0 = game.teams.all()[0]
                t1 = game.teams.all()[1]
                if i > 1:
                    p0 = Position.objects.create(matchday=i, team=t0.team, competition=game.competition)
                    p1 = Position.objects.create(matchday=i, team=t1.team, competition=game.competition)
                    p00 = Position.objects.get(matchday=(i-1), team=t0.team, competition=game.competition)
                    p11 = Position.objects.get(matchday=(i-1), team=t1.team, competition=game.competition)
                else:
                    p0 = Position.objects.create(matchday=1, team=t0.team, competition=game.competition)
                    p1 = Position.objects.create(matchday=1, team=t1.team, competition=game.competition)
                    p00 = Position.objects.create(matchday=0, team=t0.team, competition=game.competition)
                    p11 = Position.objects.create(matchday=0, team=t1.team, competition=game.competition)
                p0.goal_for = p00.goal_for + t0.goals
                p1.goal_for = p11.goal_for + t1.goals
                p0.goal_against = p00.goal_against + t1.goals
                p1.goal_against = p11.goal_against + t0.goals
                p0.goal_diff = p00.goal_for - p11.goal_against
                p1.goal_diff = p11.goal_for - p11.goal_against
                p0.fantapunti = p00.fantapunti + t0.fantapunti
                p1.fantapunti = p11.fantapunti + t1.fantapunti
                p0.played = p00.played + 1
                p1.played = p11.played + 1
                if t0.goals > t1.goals:
                    p0.wins = p00.wins + 1
                    p1.wins = p11.wins
                    p0.draws = p00.draws
                    p1.draws = p11.draws
                    p1.points = p11.points
                    p0.points = p00.points + 3
                    p1.losses = p11.losses + 1
                    p0.losses = p00.losses
                elif t0.goals < t1.goals:
                    p0.draws = p00.draws
                    p1.draws = p11.draws
                    p0.points = p00.points
                    p1.points = p11.points + 3
                    p1.wins = p11.wins + 1
                    p0.wins = p00.wins
                    p1.losses = p11.losses
                    p0.losses = p00.losses + 1
                elif t0.goals == t1.goals:
                    p0.draws = p00.draws + 1
                    p1.draws = p11.draws + 1
                    p0.points = p00.points + 1
                    p1.points = p11.points + 1
                    p0.losses = p00.losses                 
                    p1.losses = p11.losses
                    p0.wins = p00.wins                 
                    p1.wins = p11.wins                 
                p0.save()
                p1.save()
                p00.save()
                p11.save()
                s.positions.add(p0)
                s.positions.add(p1)
            s.save()     