with open('/Users/Tommi/Dev/Data/fantagazzetta_stats/scrapy_spiders/roster/teams.jl', 'r') as fp:
    for line in fp:
        j = json.loads(line)
        if j['obj'] == 'roster':
            t = Team.objects.get(name=j['team_name'])
            for i in range(len(j['players']['player'])):
                try:
                    p = Player.objects.get(name=j['players']['player'][i])
                except:
                    Player.objects.create(name=j['players']['player'][i], teamirl=j['players']['team'][i])
                    p = Player.objects.get(name=j['players']['player'][i])
                    for role in j['players']['roles'][i]:
                        r = Role.objects.get(role=role)
                        p.roles.add(r)
                        p.save()
                t.yearroster.add(p)
                t.save()
                