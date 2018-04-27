# calculates fantavoto for performance
from albo.models import *
performances = Performance.objects.filter(fantavote=None)
for perf in performances:
    if perf.vote is None:
        continue
    else:
        bonuses = 0
        if perf.bonus:
            for b in perf.bonus.all():
                bonuses += b.value
        perf.fantavote = perf.vote + bonuses
        perf.save()