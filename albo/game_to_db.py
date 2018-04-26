import uuid
import base64
import json
from albo.models import *
dcomps = {174190: "Ekstraklasa - 2018", 390305: "La Supercoppa - 2018", 174169: "Serie A - 2018", 367731: "Champions League - 2018", 367725: "Coppa delle Coppe - 2018", 367732: "Europa League - 2018", 367733: "Intertoto - 2018"}
with open('/Users/Tommi/Dev/Data/fantagazzetta_stats/scrapy_spiders/roster/games.jl', 'r') as fp:
    for line in fp:
        j = json.loads(line)
        try:
            c = Competition.objects.get(name=dcomps[j['competition']])
        except:
            continue
        matchday = j['matchday']
        home_formation = j['home_formation']
        try:
            more_info = j['more_info']
        except:
            more_info = ''
        home_formation_applied = None
        if j['home_formation_applied']:
            home_formation_applied = j['home_formation_applied']
        pseudoid = str(uuid.uuid4())
        pseudoid_m = str(uuid.uuid4())
        Game.objects.create(competition=c, matchday=matchday, pseudoid_game=pseudoid, more_info=more_info)
        game = Game.objects.get(competition=c, matchday=matchday, pseudoid_game=pseudoid)
        t = Team.objects.get(name=j['home_team'])
        MatchRoster.objects.create(team=t, home=1, matchday=matchday, formation=home_formation, formation_applied=home_formation_applied, pseudoid_match=pseudoid_m)
        for player in j['home_players']:
            home = MatchRoster.objects.get(team=t, home=1, matchday=matchday, pseudoid_match=pseudoid_m)
            try:
                p = Player.objects.get(name=player['name'].upper())
            except:
                Player.objects.create(name=player['name'].upper(), teamirl=player['team'].upper())
                p = Player.objects.get(name=player['name'].upper())
                for role in player['roles']:
                    r = Role.objects.get(role=role)
                    p.roles.add(r)
                    p.save()
            vote = None                            
            fantavote = None               
            if player['vote']:                                    
                vote = player['vote']          
            if player['fantavote']:            
                fantavote = player['fantavote']
            malus = 0          
            if player['malus']:
                malus = 1                                                                                                    
            bench = 0                                                                                                        
            if player['bench']:                                                                                              
                bench = 1
            perf_id = str(uuid.uuid4())                                                                                          
            Performance.objects.create(player=p, vote=vote, fantavote=fantavote, malus=malus, bench=bench, matchday=matchday, perf_id=perf_id)
            perf = Performance.objects.get(player=p, matchday=matchday, perf_id=perf_id)
            if player['bonus']:
                for bonus in player['bonus']:                                                
                    b = Bonus.objects.get(name=bonus)
                    perf.bonus.add(b)
                    perf.save()
            home.players.add(perf)
            home.save()
        game.teams.add(MatchRoster.objects.get(team=t, home=1, matchday=matchday, pseudoid_match=pseudoid_m))
        game.save()
        t = Team.objects.get(name=j['away_team'])
        away_formation = j['away_formation']
        away_formation_applied = None
        pseudoid_m = str(uuid.uuid4())
        if j['away_formation_applied']:
            away_formation_applied = j['away_formation_applied']
        MatchRoster.objects.create(team=t, home=0, matchday=matchday, formation=away_formation, formation_applied=away_formation_applied, pseudoid_match=pseudoid_m)
        for player in j['away_players']:
            away = MatchRoster.objects.get(team=t, home=0, matchday=matchday, pseudoid_match=pseudoid_m)
            try:
                p = Player.objects.get(name=player['name'].upper())
            except:
                Player.objects.create(name=player['name'].upper(), teamirl=player['team'].upper())
                p = Player.objects.get(name=player['name'].upper())
                for role in player['roles']:
                    r = Role.objects.get(role=role)
                    p.roles.add(r)
                    p.save()
            vote = None                            
            fantavote = None               
            if player['vote']:                                    
                vote = player['vote']          
            if player['fantavote']:            
                fantavote = player['fantavote']
            malus = 0          
            if player['malus']:
                malus = 1                                                                                                    
            bench = 0                                                                                                        
            if player['bench']:                                                                                              
                bench = 1                                                                                            
            perf_id = str(uuid.uuid4())        
            Performance.objects.create(player=p, vote=vote, fantavote=fantavote, malus=malus, bench=bench, matchday=matchday, perf_id=perf_id)
            perf = Performance.objects.get(player=p, matchday=matchday, perf_id=perf_id)
            if player['bonus']:
                for bonus in player['bonus']:                                                
                    b = Bonus.objects.get(name=bonus)
                    perf.bonus.add(b)
                    perf.save()
            away.players.add(perf)
            away.save()
        game.teams.add(MatchRoster.objects.get(team=t, home=0, matchday=matchday, pseudoid_match=pseudoid_m))
        game.save()