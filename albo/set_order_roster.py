# set order of roster
# por > d > c > a
from albo.models import *
players = Player.objects.all()
for p in players:
    if p.roles.all()[0].role=='Por':
        p.toorder = 1 
        p.save()
    elif p.roles.all()[0].role in ['Dc', 'Ds', 'Dd']:
        p.toorder = 2
        p.save()
    elif p.roles.all()[0].role in ['M', 'C', 'E']:
        p.toorder = 3
        p.save()
    elif p.roles.all()[0].role in ['T', 'W']:
        p.toorder = 4
        p.save()
    elif p.roles.all()[0].role in ['A', 'Pc']:
        p.toorder = 5
        p.save()