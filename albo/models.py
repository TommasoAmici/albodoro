from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Role(models.Model):
    role = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.role
    
    def position(self):
        if self.role == 'Por':
            return 1
        elif self.role in ['Dc', 'Dd', 'Ds']:
            return 2
        elif self.role in ['M', 'C', 'E']:
            return 3
        elif self.role in ['T', 'W']:
            return 4
        elif self.role in ['A', 'Pc']:
            return 5


class Player(models.Model):
    name = models.CharField(max_length=50)
    teamirl = models.CharField(max_length=50)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team')
    history = models.TextField(blank=True)
    yearroster = models.ManyToManyField(Player)
    logo = models.TextField(null=True)
    jersey = models.TextField(null=True)
    stadium = models.TextField(null=True)

    def __str__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date won', null=True)
    participants = models.ManyToManyField(User, related_name='participant')
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.split(' -')[0]


class Bonus(models.Model):
    name = models.CharField(max_length=200)
    value = models.FloatField(null=True)

    def __str__(self):
        return self.value


class Performance(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    vote = models.FloatField(null=True)
    fantavote = models.FloatField(null=True)
    bench = models.IntegerField(null=True)
    malus = models.IntegerField(null=True)
    bonus = models.ManyToManyField(Bonus)
    matchday = models.IntegerField(null=True)
    perf_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.player.name


class MatchRoster(models.Model):
    players = models.ManyToManyField(Performance)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_main')
    home = models.IntegerField(null=True)
    formation = models.CharField(max_length=4, null=True)
    formation_applied = models.CharField(max_length=4, null=True)
    matchday = models.IntegerField(null=True)
    pseudoid_match = models.CharField(max_length=100, null=True)
    fantapunti = models.FloatField(null=True)
    goals = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.team.name

    class Meta:
        ordering = ('home',)


class Game(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    date = models.DateTimeField('date played', null=True)
    teams = models.ManyToManyField(MatchRoster)
    matchday = models.IntegerField(null=True)
    pseudoid_game = models.CharField(max_length=100, null=True)

    def __str__(self):
        return 'giornata {}'.format(self.pseudoid_game)

    class Meta:
        ordering = ('matchday',)
